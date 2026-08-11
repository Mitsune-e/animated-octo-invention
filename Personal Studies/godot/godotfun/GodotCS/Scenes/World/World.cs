using Godot;
using System;

public partial class World : Node2D
{

	[Export] private Wizard _wizard;
	[Export] private Hobbit _hobbit;
	public override void _Ready()
	{
		//GD.Print("World ready " + GetInstanceId());
		//_wizard.CastSpell += DamageHobbit;
		_hobbit.KillWizard += DamageWizard;
	}
	
	public override void _Process(double delta)
	{
		
	}

	private void DamageHobbit()
	{
		_hobbit.SetProcess(false);
		_hobbit.Scale = new Vector2(0.3f, 0.2f);	
	}

	private void DamageWizard()
	{
		//_wizard.SetProcess(false);
		_wizard.Scale = new Vector2(0.3f, 0.2f);	
	}
}
