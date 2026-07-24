static const char norm_fg[] = "#c9c8c8";
static const char norm_bg[] = "#272326";
static const char norm_border[] = "#7c6570";

static const char sel_fg[] = "#c9c8c8";
static const char sel_bg[] = "#A3929A";
static const char sel_border[] = "#c9c8c8";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
};
