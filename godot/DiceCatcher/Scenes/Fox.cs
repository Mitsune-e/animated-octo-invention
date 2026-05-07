using Godot;
using System;

public partial class Fox : Area2D
{

	[Signal] public delegate void PointScoredEventHandler();
	[Export] private Sprite2D _foxSprite;
	private const float SPEED = 150.0f;
	private AudioStreamPlayer eatAudio;
    private float _move;

    public override void _Ready()
	{		
		eatAudio = GetNode<AudioStreamPlayer>("EatAudio");
	}

	public override void _Process(double delta)
	{
		_move = Input.GetAxis("ui_left", "ui_right");
		if (!Mathf.IsZeroApprox(_move)) {
			_foxSprite.FlipH = _move > 0.0f;
		}
	}

	public override void _PhysicsProcess(double delta)
	{
		Position += new Vector2(_move *(float)delta * SPEED, 0);
		
	}
	private void _on_Fox_area_entered(Area2D area)
	{
		if (area is Dice)
		{
			area.QueueFree();
			eatAudio.Play();
			EmitSignal("PointScored");	
		}
	}
}
