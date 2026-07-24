const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#272326", /* black   */
  [1] = "#A3929A", /* red     */
  [2] = "#D1B0B5", /* green   */
  [3] = "#D1B4CB", /* yellow  */
  [4] = "#D8B6D9", /* blue    */
  [5] = "#E9BACA", /* magenta */
  [6] = "#F2CED2", /* cyan    */
  [7] = "#c9c8c8", /* white   */

  /* 8 bright colors */
  [8]  = "#7c6570",  /* black   */
  [9]  = "#A3929A",  /* red     */
  [10] = "#D1B0B5", /* green   */
  [11] = "#D1B4CB", /* yellow  */
  [12] = "#D8B6D9", /* blue    */
  [13] = "#E9BACA", /* magenta */
  [14] = "#F2CED2", /* cyan    */
  [15] = "#c9c8c8", /* white   */

  /* special colors */
  [256] = "#272326", /* background */
  [257] = "#c9c8c8", /* foreground */
  [258] = "#c9c8c8",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
