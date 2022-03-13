/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     PROGRAM = 258,
     VAR = 259,
     PRINT = 260,
     INT = 261,
     FLOAT = 262,
     IF = 263,
     ELSE = 264,
     ID = 265,
     SEMICOLON = 266,
     PLUS = 267,
     MINUS = 268,
     DIVIDE = 269,
     MULTIPLY = 270,
     EQUALS = 271,
     OPENPARENTHESES = 272,
     CLOSEPARENTHESES = 273,
     DOT = 274,
     TWODOTS = 275,
     OPENBRACE = 276,
     CLOSEBRACE = 277,
     DIFFERENT = 278,
     GREATER = 279,
     LESS = 280,
     CTEF = 281,
     CTEI = 282,
     CTESTRING = 283
   };
#endif
/* Tokens.  */
#define PROGRAM 258
#define VAR 259
#define PRINT 260
#define INT 261
#define FLOAT 262
#define IF 263
#define ELSE 264
#define ID 265
#define SEMICOLON 266
#define PLUS 267
#define MINUS 268
#define DIVIDE 269
#define MULTIPLY 270
#define EQUALS 271
#define OPENPARENTHESES 272
#define CLOSEPARENTHESES 273
#define DOT 274
#define TWODOTS 275
#define OPENBRACE 276
#define CLOSEBRACE 277
#define DIFFERENT 278
#define GREATER 279
#define LESS 280
#define CTEF 281
#define CTEI 282
#define CTESTRING 283




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

