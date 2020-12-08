using AInvaderGame;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;

namespace AInvaderGame
{
    public class Projectile : Object
    {

		public const int kProjectileInterval = 5;
		public int ProjectileInterval = kProjectileInterval;
		public bool EntityType;

		public Projectile(int x, int y, bool type)
		{
			ImageBounds.Width = 5;
			ImageBounds.Height = 15;
			Position.X = x;
			Position.Y = y;
			EntityType = type;
		}

		public void Reset()
		{
			if (Form1.ActiveForm != null)
			{
				Position.Y = Form1.ActiveForm.ClientRectangle.Bottom;
				MovingBounds.Y = Position.Y;

			}

			ProjectileInterval = kProjectileInterval;
			UpdateBounds();
		}



		/// <summary>
		/// This will reset the projectile for the entity
		/// </summary>
		public void ResetBomb(int yPos)
		{
			Position.Y = yPos;
			ProjectileInterval = kProjectileInterval;
			UpdateBounds();
		}

		public void BulletReset()
		{
			Position.Y = Position.Y - Position.Y;
			ProjectileInterval = kProjectileInterval;
			UpdateBounds();
		}

		public override void Draw(Graphics g)
		{

			if (EntityType) { 
				UpdateBounds();
				g.FillRectangle(Brushes.Chartreuse, MovingBounds);
				Position.Y -= kProjectileInterval;
			}
			if (!EntityType)
            {
				UpdateBounds();
				g.FillRectangle(Brushes.Chartreuse, MovingBounds);
				Position.Y += kProjectileInterval;
			}
		}
	}
}
