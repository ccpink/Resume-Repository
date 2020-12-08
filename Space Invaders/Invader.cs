using AInvaderGame;
using System;
using System.Drawing;

namespace AInvaderGame
{
	public class Invader : Object
	{
		private Image OtherImage = null;
		private const int kBombInterval = 200;
		private Projectile Bomb = new Projectile(0, 0, false);
		private bool ActiveBomb = false;
		public bool BeenHit = false;
		public bool Died = false;
		public bool Direction = true;
		private const int kInterval = 10;
		private long Counter = 0;
		private bool Chance;
		private int Counter2 = 25;

		/// <summary>
		/// Constructor for invader
		/// </summary>
		public Invader(string i1, string i2) : base("C:\\Users\\ccpin\\source\\repos\\AInvaderGame\\AInvaderGame\\Assets\\invader1.gif")
		{
			OtherImage = Image.FromFile("C:\\Users\\ccpin\\source\\repos\\AInvaderGame\\AInvaderGame\\Assets\\invader1.gif");
			Position.X = 20;
			Position.Y = 10;
			UpdateBounds();
		}

		public Invader() 
		{
		}

		/// <summary>
		/// Drawing the invader and updating the bounds
		/// </summary>
		public override void Draw(Graphics g, int random)
		{
			UpdateBounds();
			Counter2 += 1;

			if (BeenHit)
			{
				return;
			}
			if (Counter % 2 == 0)
				g.DrawImage(TheImage, MovingBounds, 0, 0, 
					ImageBounds.Width, ImageBounds.Height, 
					GraphicsUnit.Pixel);
			else
				g.DrawImage(OtherImage, MovingBounds, 0, 0, 
					ImageBounds.Width, ImageBounds.Height, 
					GraphicsUnit.Pixel);

			if (ActiveBomb)
			{
				Bomb.Draw(g);
				if (Form1.ActiveForm != null)
				{
					if (Bomb.Position.Y > 
						Form1.ActiveForm.ClientRectangle.Height)
					{
						ActiveBomb = false;
						
					}
				}
			}

			

			if ((ActiveBomb == false) && 15 > random)
			{
				ActiveBomb = true;
				ResetBombPosition();
				Bomb.Position.X = MovingBounds.X + MovingBounds.Width / 2;
				Bomb.Position.Y = MovingBounds.Y + 5;
				Counter2 = 0;
			}

		}

		

		public void ResetBombPosition()
		{// Reset the bomb position
			Bomb.Position.X = MovingBounds.X + MovingBounds.Width / 2;
			Bomb.ResetBomb(MovingBounds.Y + 5);
		}


		public void Move()
		{
			if (BeenHit)
				return;

			if (Direction)
			{// True is Right
				Position.X += kInterval;
			}
			else
			{// False is Left
				Position.X -= kInterval;
			}

			// Counter for bomb incrementing
			Counter++;
		}
		public void MoveInPlace()
		{
			Counter++;
		}




		/// <summary>
		/// Counter for when the invader can throw down bombs
		/// </summary>
		public void SetCounter(long lCount)
		{
			Counter = lCount;
		}

		/// <summary>
		/// If Killed Set The Invader as dead
		/// </summary>

		public void Killed(Graphics g)
		{

			if (Died)
				return;

			Died = true;
		}

		public Rectangle GetBombBounds()
		{
			return Bomb.GetBounds();
		}



		// Check if it is colliding with anything
		public bool IsBombColliding(Rectangle AnObject)
		{
			if (ActiveBomb && Bomb.GetBounds().IntersectsWith(AnObject))
			{
				ActiveBomb = false;
				return true;
			}

			return false;
		}





	}
}
