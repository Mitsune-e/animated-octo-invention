# ...existing code...
import os

def ask(prompt, default=None):
    val = input(f"{prompt}" + (f" [{default}]" if default else "") + ": ").strip()
    return val if val else (default or "")

def read_fields_interactive():
    print("Enter fields one by line. Empty line to finish.")
    print("For each field you'll be asked: column name, data type (s=string,n=number,d=date), source type:")
    print("  source types: find -> Drr(findcolumnxls(...)).ToString")
    print("                row  -> replacechr(getrow(findcolumnxls(...), Drr))")
    print("                ref  -> replacechr(pVar.ToString)  (you must provide pVar name)")
    fields = []
    idx = 1
    while True:
        name = input(f"{idx}) Field name (or Enter to finish): ").strip()
        if not name:
            break
        dtype = ask("   type (s/n/d)", "s").lower()
        while dtype not in ("s", "n", "d"):
            dtype = ask("   invalid. type (s/n/d)", "s").lower()
        source = ask("   source (find/row/ref)", "row").lower()
        while source not in ("find", "row", "ref"):
            source = ask("   invalid. source (find/row/ref)", "row").lower()
        colname = None
        pvar = None
        if source in ("find", "row"):
            colname = ask("   column name in XLS (press Enter to use field name)", name)
        else:
            pvar = ask("   pVariable name (example pMethod)").strip()
            if not pvar:
                print("   pVariable required for source=ref. Try again.")
                continue
        fields.append({
            "name": name,
            "type": dtype,
            "source": source,
            "col": colname or name,
            "pvar": pvar
        })
        idx += 1
    return fields

def vb_expr_for_source(field):
    # Return the inner VB expression (without surrounding quotes for strings)
    col = field["col"]
    src = field["source"]
    if src == "find":
        # uses Drr(findcolumnxls(...)).ToString as in your examples
        return f'Drr(findcolumnxls("{col}")).ToString'
    if src == "row":
        # wrap with replacechr as your code expects
        return f'replacechr(getrow(findcolumnxls("{col}"), Drr))'
    # ref -> use provided pVar
    return f'replacechr({field["pvar"]}.ToString)'

def format_insert_segment(field):
    # produce a VB expression for the value (no surrounding commas)
    inner = vb_expr_for_source(field)
    # strings and dates must be quoted inside SQL (single quotes), numbers not
    if field["type"] in ("s", "d"):
        # produce VB fragment: "'" & <inner> & "'" (double quotes around single-quote as in other snippets)
        return f"\"'\" & {inner} & \"'\""
    return inner  # numeric: no single quotes

def format_update_assignment(field, wrap_date_reformat=False):
    inner = vb_expr_for_source(field)
    col = field["name"]
    if field["type"] == "d" and wrap_date_reformat:
        return f"{col}= '\" & DateReformat({inner}) & \"'"
    if field["type"] in ("s", "d"):
        return f"{col}= '\" & {inner} & \"'"
    return f"{col}= \" & {inner} & \""

def generate_vb_snippet(table, pk, fields, wrap_date_reformat=False, pk_use_find=True):
    lines = []
    # Normalize fields: remove duplicates (case-insensitive), preserve order
    seen = set()
    uniq_fields = []
    for f in fields:
        key = f["name"].strip().lower()
        if key in seen:
            continue
        seen.add(key)
        uniq_fields.append(f)
    fields = uniq_fields

    # Ensure PK present; if not, add as a 'find' source at front
    if not any(f["name"].strip().lower() == pk.strip().lower() for f in fields):
        fields.insert(0, {"name": pk, "type": "s", "source": "find", "col": pk, "pvar": None})

    # Build CheckExist using PK with Drr(findcolumnxls(...))
    lines.append(f'pFind = CheckExist("Select 1 from {table} where {pk}= \'\" & Drr(findcolumnxls(\"{pk}\")).ToString & \"\'")')
    lines.append("If pFind = False Then")

    # INSERT: column list excludes duplicates and keeps order
    col_list = ", ".join([f["name"] for f in fields])

    # Build VALUES concatenation carefully:
    # We create a list of per-field expressions: for strings -> "'" & expr & "'", for numbers -> expr
    exprs = [format_insert_segment(f) for f in fields]

    # Now join with ' & "," & ' so commas appear correctly between items.
    if exprs:
        vb_concat = exprs[0]
        for e in exprs[1:]:
            vb_concat = f'{vb_concat} & "," & {e}'
    else:
        vb_concat = '""'

    # Insert line with a newline/indent to make it readable
    lines.append(f'    InsertUpdateReco("INSERT {table} ({col_list}) VALUES (" &')
    lines.append(f'                     {vb_concat} & ")")')
    lines.append("Else")
    # UPDATE: build SET clause excluding PK
    set_parts = []
    for f in fields:
        if f["name"].strip().lower() == pk.strip().lower():
            continue
        set_parts.append(format_update_assignment(f, wrap_date_reformat))
    set_clause = ", ".join(set_parts) if set_parts else '/* no columns to update */'
    lines.append(f'    If CBUpdate.Checked = True Then InsertUpdateReco("Update {table} SET {set_clause} where {pk}= \'\" & Drr(findcolumnxls(\"{pk}\")).ToString & \"\'")')
    lines.append("End If")
    lines.append("End If")
    return "\r\n".join(lines)

def main():
    print("VB Insert/Update generator — outputs a .txt file with the VB snippet.")
    table = ask("Table name (e.g. SSTN_Assay)", "SSTN_Assay")
    pk = ask("Primary key column name (e.g. SampleID or DHID)", "SampleID")
    print("")
    fields = read_fields_interactive()
    wrap_date = ask("Wrap dates with DateReformat(...) in UPDATE? (y/N)", "N").lower() == "y"

    snippet = generate_vb_snippet(table, pk, fields, wrap_date_reformat=wrap_date)
    fname = f"{table}_insert_update.txt"
    with open(fname, "w", encoding="utf-8") as f:
        f.write(snippet)
    print(f"Generated VB snippet saved to {os.path.abspath(fname)}")

if __name__ == "__main__":
    main()
# ...existing code...