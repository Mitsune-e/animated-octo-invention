using Godot;
using System;

public partial class Game : Node2D
{
	private const float MARGIN = 80.0f; 
	[Export] private Fox _fox;
	[Export] private PackedScene _diceScene;
	[Export] private Label _scoreLabel;
	[Export] private Timer _spawnTimer;
	private int _points = 0;

	public override void _Ready()
	{
		_fox.PointScored += OnPointScored;
		_spawnTimer.Timeout += SpawnDice;
		SpawnDice();
	}

	public override void _Process(double delta)
	{
	}

	private void SpawnDice()
	{
		Dice newDice = _diceScene.Instantiate<Dice>();
		Rect2 vpr = GetViewportRect();
		float new_x = (float)GD.RandRange(vpr.Position.X + MARGIN, vpr.End.X - MARGIN);
		newDice.Position = new Vector2(new_x, -MARGIN);
		AddChild(newDice);
	}
	private void OnPointScored()
	{
		_points += 1;
		GD.Print($"Current Score: {_points}");
		_scoreLabel.Text = _points.ToString("D4");
	}
}
