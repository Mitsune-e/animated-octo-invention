using Godot;
using System;

public partial class Tappy : CharacterBody2D
{
	// Called when the node enters the scene tree for the first time.
	//private float _gravity = 200.0f;
	[Export] private AnimatedSprite2D _animatedSprite;
	const float JUMP_POWER = -350.0f;
	private float _gravity = ProjectSettings.GetSetting("physics/2d/default_gravity").AsSingle();
	private bool _jumped = false;

    public override void _UnhandledInput(InputEvent @event)
    {
		//aaa
		/* if (@event.IsActionPressed("Jump"))
		{
			_jumped = true;
		} */
    }

	
	public override void _Ready()
	{
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _PhysicsProcess(double delta)
	{
		
		Vector2 velocity = Velocity;

		velocity.Y += (float)delta * _gravity;

		/* if (_jumped)
		{
			velocity.Y = JUMP_POWER;
			_jumped = false;
		}  */
		
		if (Input.IsActionPressed("Jump"))
		{
			velocity.Y = JUMP_POWER;
		}

		Velocity = velocity;

		MoveAndSlide();

		if (IsOnFloor())
		{
			GD.Print("On Floor");
			Die();
		}
	}
	private void Die()
	{
		SetPhysicsProcess(false);
		_animatedSprite.Stop();
		
	}
}
