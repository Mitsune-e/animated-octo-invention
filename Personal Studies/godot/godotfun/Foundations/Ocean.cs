using Godot;
using System;
using System.Numerics;

public partial class Ocean : Node2D
{
	//[Export] private NodePath _planeSpritePath;
	[Export] private Sprite2D _planeSprite;
	[Export] private Sprite2D _heliSprite;
	//private Sprite2D _planeSprite;
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		GD.Print("Sucess!");
		//_planeSprite = GetNode<Sprite2D>(_planeSpritePath);
		//GD.Print($"Plane at {_planeSprite.Position}");
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		if (Input.IsActionPressed("ui_up"))
		{
		/* _planeSprite.Position = new Vector2 ( _planeSprite.Position.X + 50.0f * (float)delta, _planeSprite.Position.Y);
		_heliSprite.Position = new Vector2 (_heliSprite.Position.X + 50.0f * (float)delta, _heliSprite.Position.Y ); */
		//_planeSprite.Position += _planeSprite.Transform.X * 100.0f * (float)delta;
		_planeSprite.MoveLocalX(100.0f * (float)delta, true);
		}
		if (Input.IsActionPressed("ui_right"))
		{
			_planeSprite.Rotation += 2 * Mathf.Pi * (float)delta;
		}
		if (Input.IsActionPressed("ui_left"))
		{
			_planeSprite.Rotation -= 2 *Mathf.Pi * (float)delta;
		}
		if (Input.IsActionPressed("ui_down"))
		{
			/* _heliSprite.Position = new Vector2 (_heliSprite.Position.X, _heliSprite.Position.Y + 50.0f * (float)delta);
			_planeSprite.Position = new Vector2 ( _planeSprite.Position.X , _planeSprite.Position.Y + 50.0f * (float)delta); */
		}
		
	}
}
