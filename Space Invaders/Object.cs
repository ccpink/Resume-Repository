using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;


namespace AInvaderGame
{
    public class Object
    {
        protected Image TheImage = null; // Get image for invader/defender
        public Point Position = new Point(50, 50);
        protected Rectangle ImageBounds = new Rectangle(0, 0, 10, 10);
        protected Rectangle MovingBounds = new Rectangle();

        public Object(string fileName)
        {
            TheImage = Image.FromFile(fileName);
            ImageBounds.Width = TheImage.Width;
            ImageBounds.Height = TheImage.Height;
        }

        public Object()
        {
            TheImage = null;
        }


        public int Width{
            get{return ImageBounds.Width;}
        }

        public int Height{
            get{return ImageBounds.Height;}
        }


        public virtual int GetWidth()
        {
            return ImageBounds.Width;
        }

        public Image GetImage()
        {
            return TheImage;
        }

        public virtual Rectangle GetBounds()
        {
            return MovingBounds;
        }

        public void UpdateBounds()
        {
            MovingBounds = ImageBounds;
            MovingBounds.Offset(Position);
        }


        public virtual void Draw(Graphics g)
        {
            UpdateBounds();
            g.DrawImage(TheImage, MovingBounds, 0, 0, ImageBounds.Width, ImageBounds.Height, GraphicsUnit.Pixel);
        }

        public virtual void Draw(Graphics g, int random)
        {
            UpdateBounds(); 
            g.DrawImage(TheImage, MovingBounds, 0, 0, ImageBounds.Width, ImageBounds.Height, GraphicsUnit.Pixel);
        }


    }
}