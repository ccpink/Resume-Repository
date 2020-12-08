using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;

namespace AInvaderGame
{
    class Defender : Object
    {

		private int kInterval = 5; // Interval of movement.
		public bool Alive = true; // Is Alive or Not
		public bool BeenHit = false; // If its been hit or not

		public Defender() : base("C:\\Users\\ccpin\\source\\repos\\AInvaderGame\\AInvaderGame\\Assets\\defender.gif")
		{
			Position.X = 200;
			Position.Y = 400;

		}

		public override void Draw(Graphics g)
		{
			if (!Alive)
				return;
			if (BeenHit == false)
			{
				base.Draw(g);
			}
			else
			{
				Alive = false;
			}
		}

		public Point GetBulletStart()
		{
			Point theStart = new Point
				(
					MovingBounds.Left + MovingBounds.Width / 2,
					MovingBounds.Top - 10
				);

			return theStart;
		}

		public void MoveLeft()
		{
			Position.X -= kInterval;
			if (Position.X < 0)
				Position.X = 0;
		}

		public void MoveRight(int nLimit)
		{
			Position.X += kInterval;
			if (Position.X > nLimit - Width)
				Position.X = nLimit - Width;
		}

		public void Reset()
		{
			BeenHit = false;
			Alive = true;
		}


	}
}
