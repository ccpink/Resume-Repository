using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AInvaderGame
{
	public partial class Form1 : Form
    {
		private long TimerCounter = 0;
		private int TheSpeed = 6;

		/// <summary>
		/// How many rows and columns of invaders
		/// Num of shields
		/// </summary>
		private Endings ending = new Endings(50, 50, false, false);
		private int row = 4;
		private int column = 8;


		private int totalInvaders;
		/// <summary> 
		/// Game objects
		/// </summary>

		private bool ActiveBullet = false;
		private Defender TheDefender = null;
		private bool GameGoing = true;
		private Projectile TheBullet = new Projectile(20, 30, true);
		private InvaderControl InvaderCon;

		/// <summary>
		/// What key is being held down
		/// </summary>
		private string CurrentKeyDown = "";
		private string LastKeyDown = "";


		public Form1()
        {
            InitializeComponent();
			
			/// Optimization.
            SetStyle(ControlStyles.UserPaint, true);
            SetStyle(ControlStyles.AllPaintingInWmPaint, true);
            SetStyle(ControlStyles.OptimizedDoubleBuffer, true);
            InitializeGame(true);

            timer2.Start();
        }

        private void InitializeGame(bool bScore)
        {
            InitializeMan();
			InitializeInvaderRows(row, column);
        } 

		/// <summary>
		/// Create the Defender
		/// </summary>
		private void InitializeMan()
		{
			TheDefender = new Defender();
			TheDefender.Position.Y = ClientRectangle.Bottom - 50;
		}


		/// <summary>
		/// Create the invaders
		/// </summary>
		void InitializeInvaderRows(int row, int column)
		{ 
			InvaderCon = new InvaderControl(row, column, "invader1.gif", "invader1.gif");
		}

		
		/// <summary>
		/// User Input for the defender
		/// </summary>
		private void HandleKeys()
		{
			switch (CurrentKeyDown)
			{
				case "Space":
					if (ActiveBullet == false)
					{
						TheBullet.Position = TheDefender.GetBulletStart();
						ActiveBullet = true;
					}
					CurrentKeyDown = LastKeyDown;
					break;
				
				case "Left":
					TheDefender.MoveLeft();
					Invalidate(TheDefender.GetBounds());
					if (timer2.Enabled == false)
						timer2.Start();
					break;
				
				case "Right":
					TheDefender.MoveRight(ClientRectangle.Right);
					Invalidate(TheDefender.GetBounds());
					if (timer2.Enabled == false)
						timer2.Start();
					break;
				
				default:
					break;
			}


		}

		/// <summary>
		/// What the current key being pressed is
		/// </summary>
		private void Form1_KeyDown_1(object sender, System.Windows.Forms.KeyEventArgs e)
		{
			string result = e.KeyData.ToString();
			CurrentKeyDown = result;
			if (result == "Left" || result == "Right")
			{
				LastKeyDown = result;
			}
		}

		/// <summary>
		/// Paint all object here
		/// </summary>

		private void Form1_Paint_1(object sender, System.Windows.Forms.PaintEventArgs e)
		{
			Graphics g = e.Graphics;

			TheDefender.Draw(g);

			
			TheBullet.Draw(g);
			

			InvaderCon.Draw(g);

			
			ending.Draw(g);
			

		}


		/// <summary>
		/// Get the furthest right
		/// </summary>
		private int CalculateLargestLastPosition()
		{
			int max = 0;
			
			int nLastPos = InvaderCon.GetLastInvader().Position.X;
			if (nLastPos > max)
				max = nLastPos;
		
			return max;
		}


		/// <summary>
		/// Get the furthest left
		/// </summary>

		private int CalculateSmallestFirstPosition()
		{
			int min = 50000;

			try
			{
				
				int nFirstPos = InvaderCon.GetFirstInvader().Position.X;
				if (nFirstPos < min)
					min = nFirstPos;
				
			}
			catch (Exception ex)
			{
				MessageBox.Show(ex.Message.ToString());
			}

			return min;

		}





		/// <summary>
		/// Moving invaders
		/// </summary>
		/// 
		private int MoveCounter = 1;
		private bool Direction = true;
		private void MoveInvaders()
		{
			bool bMoveDown = false;

			InvaderCon.MoveInvaders();
		
			if (Direction == true)
            {
				MoveCounter += 1;
            } else
            {
				MoveCounter -= 1;
            }



			if (MoveCounter == 20)
			{
				InvaderCon.ChangeDirection();
				Direction = false;
			}

			if (MoveCounter == -5)
			{
				InvaderCon.ChangeDirection();
				bMoveDown = true;
				Direction = true;
			}

			if (bMoveDown)
			{
				InvaderCon.MoveDown();
			}
		}


		/// <summary>
		/// Total num of invaders left
		/// </summary>
		private int TotalNumberOfInvaders()
		{
			int sum = InvaderCon.NumberOfLiveInvaders();
			
			return sum;
		}


		/// <summary>
		/// Bullet Collision 
		/// </summary>
		void TestBulletCollision()
		{

            bool collisionIndex = InvaderCon.CheckCollision(TheBullet.GetBounds());
			int row = -1;
			int column = -1;

			


			if ((collisionIndex) && ActiveBullet)
			{
				InvaderCon.InvaderHit(row, column);
				ActiveBullet = false;
				TheBullet.BulletReset();

			}

		}
		

		/// <summary>
		/// If gameover
		/// </summary>
		void GameOver()
		{	
			if (InvaderCon.AlienHasLanded(ClientRectangle.Bottom))
			{
				TheDefender.BeenHit = true;
				GameGoing = false;
				Close();
			}
			
		}


		private void Form1_FormClosing(object sender, FormClosingEventArgs e)
		{
			string message = "The Game Is Over";
			string title = "Its Over Man";
			MessageBox.Show(message, title);

		}


		void ResetAllBombCounters()
		{
			InvaderCon.ResetAllBombCounters();			
		}

		void TestBombCollision()
		{
			if (!TheDefender.Alive)
			{
				GameGoing = false;
				ending = new Endings(500, 400, true , true);

				
				Invalidate();
		
			}

			if (TheDefender.BeenHit == true)
				return;

			if (InvaderCon.IsBombColliding(TheDefender.GetBounds()))
			{
				TheDefender.BeenHit = true;		
			}
		}

		private void timer2_Tick(object sender, System.EventArgs e)
		{
			HandleKeys();
			int count;
			TimerCounter++;

			if (GameGoing == false)
			{
				if (TimerCounter % 6 == 0)
					count = 6;

				Invalidate();
				return;
			}


			if (TheBullet.Position.Y < 0)
			{
				ActiveBullet = false;
			}



			if (TimerCounter % TheSpeed == 0)
			{
				MoveInvaders();

				totalInvaders = TotalNumberOfInvaders();

				if (totalInvaders <= 20)
				{
					TheSpeed = 5;
				}

				if (totalInvaders <= 10)
				{
					TheSpeed = 4;
				}


				if (totalInvaders <= 5)
				{
					TheSpeed = 3;
				}

				if (totalInvaders <= 3)
				{
					TheSpeed = 2;
				}

				if (totalInvaders <= 1)
				{
					TheSpeed = 1;
				}

				if (totalInvaders == 0)
				{
					this.GameGoing = false;
					ending = new Endings(500, 400, false, true);

				}
			}

			TestBulletCollision();
			TestBombCollision();


			Invalidate();
		}

		private void Form1_KeyUp_1(object sender, KeyEventArgs e)
		{
			string result = e.KeyData.ToString();
			if (result == "Left" || result == "Right")
			{
				LastKeyDown = "";
			}
			results = result;
			if (GameGoing == false)
            {
				Close();
            } 

		}

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }









}






