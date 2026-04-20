using Godot;
using System;

public partial class World : Node2D
{
	public override void _EnterTree()
	{
		//GD.Print("World entered tree " + GetInstanceId());
	}
	public override void _Ready()
	{
		//GD.Print("World ready " + GetInstanceId());
	}
	
	public override void _ExitTree()
	{
		//GD.Print("Exit Tree " + GetInstanceId());
	}

	public override void _Process(double delta)
	{
		
	}
}
