using Godot;
using System;
using System.Numerics;

public partial class Dice : Area2D
{
	[Signal] public delegate void GameOverEventHandler();
	[Export] private Sprite2D _diceSprite;
	private const float SPEED = 80.0f;
	private const float BASE_ROTATION_SPEED = 4.0f;
	
	private float _rotationSpeed = BASE_ROTATION_SPEED;
	public override void _Ready()
	{
		if(GD.Randf() < 0.5f)
		{
			_rotationSpeed = -BASE_ROTATION_SPEED;
		}
	}

    public override void _PhysicsProcess(double delta)
    {
        Position += new Godot.Vector2(0, SPEED * (float)delta);
		_diceSprite.Rotate(_rotationSpeed * (float)delta);
		GameOverCheck(); 
    }

	private void GameOverCheck()
	{
		Rect2 vpr = GetViewportRect();
		if(Position.Y > vpr.End.Y)
		{
			SetPhysicsProcess(false);
			QueueFree();
			EmitSignal("GameOver");
		}
	}
}
