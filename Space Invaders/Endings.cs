using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System;
using System.Drawing;
using System.Drawing.Imaging;

namespace AInvaderGame
{
    class Endings : Object
    {
        public bool results;
        public bool CanDraw;
        public Font MyFont = new Font("Compact", 38.0f, GraphicsUnit.Pixel);

        public Endings(int x, int y, bool result, bool canDraw)
        {
            ImageBounds.Width = 400;
            ImageBounds.Height = 400;
            Position.X = x;
            Position.Y = y;
            results = result;
            CanDraw = canDraw;
        }

        
        /// <summary>
        /// Draw somthing depending on if they win or lose
        /// </summary>
        
        public override void Draw(Graphics g)
        {
 

            if (results == false && CanDraw == true) { 
                g.FillRectangle(Brushes.Gray, MovingBounds);
                g.DrawString("You Won \n Press any key to exit", MyFont, Brushes.LimeGreen, Position.X, Position.Y, new StringFormat());
            }
            else if (results == true && CanDraw == true) { 
                g.FillRectangle(Brushes.Gray, MovingBounds);
                g.DrawString("Game Over \n Press any key to exit", MyFont, Brushes.White, Position.X - 100, Position.Y + MyFont.Height + 5, new StringFormat());
            }
        }


    }
}
