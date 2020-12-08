using System;
using System.Collections;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AInvaderGame
{
    class InvaderControl
    {
        ArrayList InvaderRows = new ArrayList();
        public Point LastPosition = new Point(0, 0);

        string gif1 = "C:\\Users\\ccpin\\source\\repos\\AInvaderGame\\AInvaderGame\\Assets\\invader1.gif";

        int Column;
        int Rows;

        ///
        /// So this will
        ///

        public InvaderControl(int Col, int Row, string gif1, string gif2) {

            this.Column = Col;
            this.Rows = Row;


            // For each row create an array of invaders that are equal to the amount of columns
            for (int i = 0; i < this.Rows; i++)
            {
                Invader[] InvaderRow = new Invader[this.Column - 1];

                for (int j = 0; j < InvaderRow.Length; j++)
                {
                    InvaderRow[j] = new Invader(gif1, gif2);
                }


                InvaderRows.Add(InvaderRow);
            }


            int rowNum = 1;
            foreach (Invader[] Invader in InvaderRows)
            {
                for (int j = 0; j < Invader.Length; j++)
                {
                    Invader[j] = new Invader(gif1, gif2);
                    Invader[j].Position.X = (rowNum * 2)  * Invader[j].GetBounds().Width + 50;
                    Invader[j].Position.Y = (j * 2 )* Invader[j].GetBounds().Height + 30;
                    Invader[j].SetCounter(rowNum * 50);

                    if (j == Invader.Length - 1)
                    {
                        LastPosition = Invader[j].Position;
                    }
                }
                rowNum++;
            }

        }

        public Invader InvaderHit(int row, int column )   // indexer declaration
        {
            
            int CurrentRow = 0;
            int CurrentColumn = 0;
            foreach (Invader[] Invader in InvaderRows)
            { 
                if (CurrentRow == row) { 
                for (int j = 0; j < Invader.Length; j++)
                {
                    if (j == column) {

                        Invader[j].BeenHit = true;
                    }

                    CurrentColumn += 1;
                }
                CurrentRow += 1;
                }
            }

            // Incase somthing happens and it can't return a invader
            Invader inv = new Invader(gif1, gif1);
            return inv;


        }


        /// <summary>
        /// Draw all Invaders
        /// </summary>
        /// 
        Random rnd = new Random();

        public void Draw(Graphics g)
        {
            foreach (Invader[] Invader in InvaderRows)
            {
                for (int j = 0; j < Invader.Length; j++)
                {
                    if ((!Invader[j].BeenHit)) { 
                        int rand = rnd.Next(1, 300);
                        Invader[j].Draw(g, rand);
                    }
                }
            }
        }


      
        /// <summary>
        /// Check if they collided with something
        /// </summary>
        /// <returns>Return what they collided with</returns>
        public bool CheckCollision(Rectangle hitBox)
        {
            
            
            foreach (Invader[] Invader in InvaderRows)
            {
                for (int j = 0; j < Invader.Length; j++)
                {
                    if ((Invader[j].GetBounds().IntersectsWith(hitBox)) && (!Invader[j].BeenHit)) {
                        bool truth = true;
                        Invader[j].Died = true;
                        Invader[j].BeenHit = true;
                        return truth;
                    }
                }
                
            }
            
            return false;
        }
        /// <summary>
        /// Change the direction of the invaders
        /// </summary>
        public void ChangeDirection()
        {
            foreach (Invader[] Invader in InvaderRows)
            {
                for (int j = 0; j < Invader.Length; j++)
                {
                    Invader[j].Direction = !Invader[j].Direction;
                }
            }
        }

        /// <summary>
        /// Move the invaders
        /// </summary>
        public void MoveInvaders()
        {
            foreach (Invader[] Invader in InvaderRows)
            {
                for (int j = 0; j < Invader.Length; j++)
                {
                    Invader[j].Move();
                }
            }
        }



        /// <summary>
        /// Move the Invaders down
        /// </summary>
        public void MoveDown()
        {

            foreach (Invader[] Invader in InvaderRows)
            {
                for (int j = 0; j < Invader.Length; j++)
                {
                    Invader[j].Position.Y += Invader[j].GetBounds().Height / 8;
                    Invader[j].UpdateBounds();
                }
            }
        }

        /// <summary>
        /// Check if the boms are colliding with anything
        /// </summary>
        public bool IsBombColliding(Rectangle rec)
        {
            foreach (Invader[] Invader in InvaderRows)
            {
                for (int j = 0; j < Invader.Length; j++)
                {
                    if (Invader[j].IsBombColliding(rec))
                    { return true; }
                }
            }

            return false;
        }


        public Invader GetLastInvader()
        {
     
            int oneGo = 0;

            Invader TheInvader = new Invader(gif1, gif1);

            foreach (Invader[] inv in InvaderRows)
            {
                if (oneGo == 0)
                {
                    int i = inv.Length;
                     TheInvader = inv[i-1];
                }
                oneGo++;
            }

            return TheInvader;
        }




        public Invader GetFirstInvader()
        {

            int oneGo = 0;

            Invader TheInvader = new Invader(gif1, gif1);

            foreach (Invader[] inv in InvaderRows)
            {
                if (oneGo == 0)
                {
                    int i = 0;
                    TheInvader = inv[i];
                }
                oneGo++;
            }

            return TheInvader;
        }




        public int GetWidth()
        {
            int Width = 0;
            int oneGo = 0;

            foreach (Invader[] inv in InvaderRows)
            { 
                if (oneGo == 0) { 
                for (int j = 0; j < inv.Length; j++)
                {
                    Width += inv[j].GetWidth();
                    Width += 110;
                }
                }
                oneGo++;
            }

            return Width;
        }

        public bool AlienHasLanded(int bottom)
        {
            foreach (Invader[] inv in InvaderRows)
            {
                for (int j = 0; j < inv.Length; j++)
                {
                    if ((inv[j].GetBounds().Bottom >= bottom) &&
                     (inv[j].BeenHit = false))
                        return true;
                }
            }

            return false;
        }



        public void ResetAllBombCounters()
        {
            foreach (Invader[] inv in InvaderRows)
            {
                for (int j = 0; j < inv.Length; j++)
                {
                    inv[j].ResetBombPosition();
                    inv[j].SetCounter(j * 50);

                }
            }

        }

        public int NumberOfLiveInvaders()
        {
            int count = 0;

            foreach (Invader[] inv in InvaderRows)
            {
                for (int j = 0; j < inv.Length; j++)
                {
                    if (inv[j].Died == false)
                    {
                        count++;
                    }

                }
            }

            return count;
        }








    }
}
