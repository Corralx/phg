import argparse, sys

def main():
	# TODO(Corralx): Help message
	parser = argparse.ArgumentParser(description='Generate platform header')
	parser.add_argument('-p', '--prefix', dest='prefix', action='store', required=True)
	parser.add_argument('-o', '--output', dest='output', action='store', required=False)
	args = parser.parse_args()
	
	# TODO(Corralx): Check file exists
	if args.output:
		output_file = open(args.output, 'w')
	else:
		output_file = sys.stdout

	# TODO(Corralx): ARM architectures
	output_file.write(
"""#pragma once

/* Platforms */
#define {0}_PLATFORM_LINUX   0
#define {0}_PLATFORM_ANDROID 0
#define {0}_PLATFORM_WINDOWS 0
#define {0}_PLATFORM_IPHONE  0
#define {0}_PLATFORM_MACOS   0

#if defined(__linux__)
#ifdef __gnu_linux__
#undef  {0}_PLATFORM_LINUX
#define {0}_PLATFORM_LINUX 1
#define {0}_PLATFORM_NAME "GNU Linux"
#elif __ANDROID__
#undef  {0}_PLATFORM_ANDROID
#define {0}_PLATFORM_ANDROID 1
#define {0}_PLATFORM_NAME "Android"
#else
#error "Unknown Linux platform!"
#endif
#elif defined(_WIN32)
#undef  {0}_PLATFORM_WINDOWS
#define {0}_PLATFORM_WINDOWS 1
#define {0}_PLATFORM_NAME "Windows"
#elif defined(__APPLE__)
#undef  {0}_PLATFORM_APPLE
#define {0}_PLATFORM_APPLE 1
#include "TargetConditionals.h"
#if TARGET_IPHONE_SIMULATOR
#undef  {0}_PLATFORM_IOS
#define {0}_PLATFORM_IOS 1
#define {0}_PLATFORM_NAME "iOS Simulator"
#elif TARGET_OS_IPHONE
#undef  {0}_PLATFORM_IOS
#define {0}_PLATFORM_IOS 1
#define {0}_PLATFORM_NAME "iOS"
#elif TARGET_OS_MAC
#undef  {0}_PLATFORM_MACOS
#define {0}_PLATFORM_MACOS 1
#define {0}_PLATFORM_NAME "Mac OSX"
#else
#error "Unknown Apple platform!"
#endif
#else
#error "Unsupported platform!"
#endif

/* Compilers */
#define {0}_COMPILER_MSVC  0
#define {0}_COMPILER_CLANG 0
#define {0}_COMPILER_GCC   0
#define {0}_COMPILER_NAME "Unknown"

#if defined(_MSC_VER)
#undef  {0}_COMPILER_MSVC
#define {0}_COMPILER_MSVC 1
#undef  {0}_COMPILER_NAME
#define {0}_COMPILER_NAME "Microsoft Visual C++"
#elif defined(__clang__)
#undef  {0}_COMPILER_CLANG
#define {0}_COMPILER_CLANG 1
#undef  {0}_COMPILER_NAME
#define {0}_COMPILER_NAME "Clang"
#elif defined(__GNUC__)
#undef  {0}_COMPILER_GCC
#define {0}_COMPILER_GCC 1
#undef  {0}_COMPILER_NAME
#define {0}_COMPILER_NAME "GCC"
#elif
#error "Unsupported compiler!"
#endif

/* Architectures */
#define {0}_ARCHITECTURE_64_BIT 0
#define {0}_ARCHITECTURE_32_BIT 0

#if {0}_PLATFORM_WINDOWS
#ifdef _WIN64
#undef  {0}_ARCHITECTURE_64_BIT
#define {0}_ARCHITECTURE_64_BIT 1
#else
#undef  {0}_ARCHITECTURE_32_BIT
#define {0}_ARCHITECTURE_32_BIT 1
#endif
#elif {0}_PLATFORM_MACOS || {0}_PLATFORM_LINUX
#ifdef __x86_64__
#undef  {0}_ARCHITECTURE_64_BIT
#define {0}_ARCHITECTURE_64_BIT 1
#else
#undef  {0}_ARCHITECTURE_32_BIT
#define {0}_ARCHITECTURE_32_BIT 1
#endif
#else
#error "Unsupported architecture!"
#endif

#define {0}_UNUSED(var)		\\
{{							\\
	do						\\
	{{						\\
		(var);				\\
	}}						\\
	while (0);				\\
}}

#define {0}_UNUSED_PARAM(param)

#define {0}_LOCAL static

#if {0}_COMPILER_MSVC
#define {0}_INTERFACE __declspec(dllexport)
#elif {0}_COMPILER_GCC || {0}_COMPILER_CLANG
#define {0}_INTERFACE __attribute__ ((visibility ("default")))
#else
#error "Unsupported compiler!"
#endif

#define {0}_ASSERT(cond) assert(cond)

/* String Concatenation */
#define {0}_CONCAT(x,y) {0}_CONCAT_AUX(x,y)
#define {0}_CONCAT_AUX(x,y) x ## y

/* Conditional Expansion */
#define {0}_IIF(c) {0}_CONCAT_AUX({0}_IIF_, c)
#define {0}_IIF_0(t, f) f
#define {0}_IIF_1(t, f) t

/* Get name of feature */
#define {0}_FEATURE(x) {0}_CONCAT_AUX({0}_FEATURE_, x)

/* Expands to expr1 if feature is 1, expr2 if feature is 0 */
#define {0}_IF_FEATURE(feature, expr1, expr2) \\
	{0}_IIF({0}_FEATURE(feature))(expr1, expr2)
""".format(args.prefix))

if __name__ == "__main__":
    main()