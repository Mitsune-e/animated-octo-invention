using Godot;
using System;

public partial class Pipes : Node2D
{
	[Export] private float pipeVelocity = 120f;
	[Export] private VisibleOnScreenNotifier2D visibleNotifier;
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
        visibleNotifier.ScreenExited += OnScreenExited;
	}
	 private void OnScreenExited()
    {
        QueueFree(); // Remove the pipe when it leaves the screen
		GD.Print("Pipe removed from scene");
    }

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}

    public override void _PhysicsProcess(double delta)
    {
        Position += Vector2.Left * pipeVelocity * (float)delta;
    }
}
