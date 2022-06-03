 public class WinAPI {
        // WinAPI Windows Load Animate
        public const int HOR_POSITIVE = 0X1;
        public const int HOR_NEGATIVE = 0X2;

        public const int VER_POSITIVE = 0X4;
        public const int VER_NEGATIVE = 0X8;

        public const int CENTER = 0X10;

        public const int BLEND = 0X80000;

        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        public static extern int AnimateWindow(IntPtr hwand, int dwTime, int dwflag);
    }

 /// Usage
    /// Init class
 WinAPI WinAPI = new WinAPI();
 private void onScreenLoad (object sender, EventArgs e) {
        WinAPI.AnimateWindow(this.Handle, 150, WinAPI.CENTER);
        this.CenterToParent();
    }