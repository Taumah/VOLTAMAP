#include <png.h>
#pragma message("Compiling with libpng version " PNG_LIBPNG_VER_STRING ".")
#if PNG_LIBPNG_VER < 10200
  #error "libpng version 1.2 or higher is required."
#endif
