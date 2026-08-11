using Godot;
using System;

public partial class Hobbit : Node2D
{
	// Called when the node enters the scene tree for the first time.
	[Signal] public delegate void KillWizardEventHandler();
	public override void _Ready()
	{
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		Rotate((float)delta * Mathf.Pi);
		if(Input.IsActionPressed("ui_up"))
		{
			// Move right.
			EmitSignal(SignalName.KillWizard);
		}
	}
}
