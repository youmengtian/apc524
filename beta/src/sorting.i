%module sorting
%{
#define SWIF_FILE_WITH_INIT
#include "sorting.h"
#include "bubble_sort.h"
#include "quick_sort.h"
%}

%include "sorting.h"
%include "bubble_sort.h"
%include "quick_sort.h"