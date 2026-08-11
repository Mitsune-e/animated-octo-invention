using Godot;
using System;

public partial class Game : Node2D
{
	private const float MARGIN = 80.0f; 
	private const string STOPPABLE_GROUP = "stoppable";
	private readonly AudioStream GAME_OVER = GD.Load<AudioStream>("res://Assets/game_over.wav");
	[Export] private Fox _fox;
	[Export] private PackedScene _diceScene;
	[Export] private Label _scoreLabel;
	[Export] private Timer _spawnTimer;
	[Export] private AudioStreamPlayer _music;
	private int _points = 0;

    public override void _UnhandledInput(InputEvent @event)
    {
        if(@event.IsActionPressed("Restart"))
		{GetTree().ReloadCurrentScene();}
    }

	public override void _Ready()
	{
		_fox.PointScored += OnPointScored;
		_spawnTimer.Timeout += SpawnDice;
		SpawnDice();
	}
	
	private void StopAll()
	{
		_spawnTimer.Stop();
		var toStop = GetTree().GetNodesInGroup(STOPPABLE_GROUP);
		foreach(Node item in toStop)
		{
			item.SetPhysicsProcess(false);
		}
	}
	private void _on_Game_over()
	{
		GD.Print("Game Over!");
		StopAll();
		_music.Stop();
		_music.Stream = GAME_OVER;
		_music.Play();
		_fox.SetProcess(false);
		_fox.SetPhysicsProcess(false);
		/* _spawnTimer.Stop();
		foreach (Node child in GetChildren())
		{
			if (child is Dice dice)
			{
				dice.SetPhysicsProcess(false);
			}
		} */
	}
	private void SpawnDice()
	{
		Dice newDice = _diceScene.Instantiate<Dice>();
		Rect2 vpr = GetViewportRect();
		float new_x = (float)GD.RandRange(vpr.Position.X + MARGIN, vpr.End.X - MARGIN);
		newDice.Position = new Vector2(new_x, -MARGIN);
		newDice.GameOver += _on_Game_over;
		AddChild(newDice);
	}
	private void OnPointScored()
	{
		_points += 1;
		GD.Print($"Current Score: {_points}");
		_scoreLabel.Text = _points.ToString("D4");
	}
}
