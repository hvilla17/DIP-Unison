/***********************************************************************
 *
 Copyright © 1995 - 1998, 3Com Corporation or its subsidiaries ("3Com").  
 All rights reserved.
   
 This software may be copied and used solely for developing products for 
 the Palm Computing platform and for archival and backup purposes.  Except 
 for the foregoing, no part of this software may be reproduced or transmitted 
 in any form or by any means or used to make any derivative work (such as 
 translation, transformation or adaptation) without express written consent 
 from 3Com.

 3Com reserves the right to revise this software and to make changes in content 
 from time to time without obligation on the part of 3Com to provide notification 
 of such revision or changes.  
 3COM MAKES NO REPRESENTATIONS OR WARRANTIES THAT THE SOFTWARE IS FREE OF ERRORS 
 OR THAT THE SOFTWARE IS SUITABLE FOR YOUR USE.  THE SOFTWARE IS PROVIDED ON AN 
 "AS IS" BASIS.  3COM MAKES NO WARRANTIES, TERMS OR CONDITIONS, EXPRESS OR IMPLIED, 
 EITHER IN FACT OR BY OPERATION OF LAW, STATUTORY OR OTHERWISE, INCLUDING WARRANTIES, 
 TERMS, OR CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND 
 SATISFACTORY QUALITY.

 TO THE FULL EXTENT ALLOWED BY LAW, 3COM ALSO EXCLUDES FOR ITSELF AND ITS SUPPLIERS 
 ANY LIABILITY, WHETHER BASED IN CONTRACT OR TORT (INCLUDING NEGLIGENCE), FOR 
 DIRECT, INCIDENTAL, CONSEQUENTIAL, INDIRECT, SPECIAL, OR PUNITIVE DAMAGES OF 
 ANY KIND, OR FOR LOSS OF REVENUE OR PROFITS, LOSS OF BUSINESS, LOSS OF INFORMATION 
 OR DATA, OR OTHER FINANCIAL LOSS ARISING OUT OF OR IN CONNECTION WITH THIS SOFTWARE, 
 EVEN IF 3COM HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

 3Com, HotSync, Palm Computing, and Graffiti are registered trademarks, and 
 Palm III and Palm OS are trademarks of 3Com Corporation or its subsidiaries.

 IF THIS SOFTWARE IS PROVIDED ON A COMPACT DISK, THE OTHER SOFTWARE AND 
 DOCUMENTATION ON THE COMPACT DISK ARE SUBJECT TO THE LICENSE AGREEMENT 
 ACCOMPANYING THE COMPACT DISK.

 *************************************************************************
 *
 * PROJECT:  HardBall
 * FILE:     HardBallLevels.h
 * AUTHOR:	 Roger Flores: Feb 8, 1996
 *
 * DECLARER: HardBall
 *
 * DESCRIPTION:
 *	  These are the commonly modified game parameters. 
 *
 **********************************************************************/


static Int BrickScores[brickTypeCount] = {0, 5, 10, 20};


#define levelCount		15
#define BE	empty
#define B1	brick1
#define B2	brick2
#define B3	brick3
#define BU	unbreakable
#define BB	ballBrick
#define BS	sidePaddleBrick



static LevelType levelInfo[levelCount] = 
	{
		// Level 0
		{
			"Portcullis",
			{BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 B2, BE, BE, B2, BE, BE, B2, BE, BE,
			 B2, B2, BE, B2, B2, BE, B2, B2, BE,
			 B1, B2, B2, B1, B2, B2, B1, B2, B2,
			 B1, B1, B2, B1, B1, B2, B1, B1, B2,
			 B1, B1, B1, B1, B1, B1, B1, B1, B1,
			 BE, B1, B1, BE, B1, B1, BE, B1, B1,
			 BE, BE, B1, BE, BE, B1, BE, BE, B1,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE}
		},
		// Diamonds - Level 1
		{
			"Diamonds",
			{B3, B3, BE, BE, B1, BE, BE, B3, B3,
			 B3, BE, BE, B1, B1, B1, BE, BE, B3,
			 BE, BE, B1, B1, B1, B1, B1, BE, BE,
			 BE, BE, B2, B1, B1, B1, B2, BE, BE,
			 BE, B2, B2, B2, B1, B2, B2, B2, BE,
			 B2, B2, B2, B2, B2, B2, B2, B2, B2,
			 B1, B2, B2, B2, B1, B2, B2, B2, B1,
			 B1, B1, B2, B1, B1, B1, B2, B1, B1,
			 B1, B1, B1, B1, B1, B1, B1, B1, B1,
			 B1, B1, BE, B1, B1, B1, BE, B1, B1,
			 B1, BE, BE, BE, B1, BE, BE, BE, B1}
		},
		// Metro - Level 2
		{
			"Metro",
			{BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 BE, BE, BE, B2, B2, B2, BE, BE, BE,
			 BE, BE, B3, B3, B2, B2, BE, BE, BE,
			 BE, BE, B3, B3, B2, B2, BE, BE, BE,
			 BE, B1, B3, BU, B2, B2, B1, B1, BE,
			 BE, B1, B3, BU, B2, B2, B1, B1, BE,
			 BE, B1, B3, BU, B2, B2, B1, B1, BE,
			 BE, B1, B1, B2, B2, B2, B1, B1, BE,
			 BE, B1, B1, B2, B2, B2, B1, B1, BE,
			 BE, B1, B1, B1, B1, B1, B1, B1, BE,
			 BE, B1, B1, B1, B1, B1, B1, B1, BE}
		},
		// Trouble Slide - Level 3
		{
			"Trouble",
			{BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 B2, B2, B2, B2, B2, B2, B1, B1, B1,
			 B3, B2, B2, B2, B2, B1, B1, B1, B1,
			 B3, B3, B2, B2, BU, B1, B1, B1, B1,
			 B3, B3, B3, BU, B1, B1, B1, B1, B1,
			 B3, B3, BU, B1, B1, B1, B1, B1, B1,
			 B3, BU, B1, B1, B1, B1, B1, B1, B1,
			 BU, B1, B1, B1, B1, B1, B1, B1, B1,
			 B1, B1, B1, B1, B1, B1, B1, B1, B1,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE}
		},
		// Egyptian - Level 4
		{
			"Desert Visions",
			{BE, BE, B3, BE, BE, BE, BE, B1, BE,
			 BE, BE, B3, BE, BE, BE, BE, B1, B1,
			 BE, B3, B3, B3, BE, B2, BE, B1, B1,
			 BE, B3, B3, B3, BE, B2, BE, BE, B1,
			 B3, B3, B3, B3, B2, B2, B2, BE, BE,
			 B3, B3, B3, B3, B2, B2, B2, B1, BE,
			 B3, B3, B3, B2, B2, B2, B2, B1, BE,
			 B3, B3, B3, B2, B2, B2, B1, B1, B1,
			 B2, B2, B2, B2, B2, B2, B1, B1, B1,
			 B1, B1, B1, B1, B1, B1, B1, B1, B1,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE}
		},
		// Double Trouble - Level 5
		{
			"Double Trouble",
			{BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 B2, B2, B2, B2, BU, BB, B3, B3, B3,
			 B2, B2, B2, B2, B2, BU, B3, B3, B3,
			 B2, B2, B2, B2, BB, B2, BU, B3, B3,
			 B2, B2, B2, B2, BU, B1, B1, BU, B3,
			 B2, B2, B2, BU, B1, B1, B1, B1, B3,
			 B2, B2, BU, B1, B1, B1, B1, B1, B1,
			 B2, BU, B1, B1, B1, B1, B1, B1, B1,
			 B2, B1, B1, B1, B1, B1, B1, B1, B1,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE}
		},
		// High V - Level 6
		{
			"High V",
			{BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 BE, B2, B2, B2, BE, B2, B2, B2, BE,
			 B2, B2, BU, B3, B3, B3, BU, B2, B2,
			 B2, B1, B1, BU, B3, BU, B1, B1, B2,
			 B1, B1, B1, B1, BU, B1, B1, B1, B1,
			 B1, B1, B1, B1, B1, B1, B1, B1, B1,
			 B1, B1, B1, B1, BB, B1, B1, B1, B1,
			 B1, B1, B1, B1, B1, B1, B1, B1, B1,
			 B1, B1, B1, B1, B1, B1, B1, B1, B1,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE}
		},
		// Mayan - Level 7
		{
			"Mayan",
			{BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 B2, B2, B2, BU, BB, BU, B2, B2, B2,
			 B2, B2, B2, B1, B1, B1, B2, B2, B2,
			 B2, B2, B1, B1, B1, B1, B1, B2, B2,
			 B2, B1, B1, B1, B1, B1, B1, B1, B2,
			 B1, B1, B1, B1, B1, B1, B1, B1, B1,
			 B1, B1, B1, B1, BB, B1, B1, B1, B1,
			 B1, B1, B1, BE, BE, BE, B1, B1, B1,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE}
		},
		// Face It - Level 8
		{
			"Face It",
			{BE, BE, B3, B3, B3, B3, B3, BE, BE,
			 BE, B2, B3, B3, B3, B3, B3, B2, BE,
			 B2, B2, B1, B3, B3, B3, B1, B2, B2,
			 B2, B1, BB, B1, B3, B1, BB, B1, B2,
			 B2, B1, BU, B1, B2, B1, BU, B1, B2,
			 B2, B2, B1, B2, B2, B2, B1, B2, B2,
			 B2, B2, B2, B2, B2, B2, B2, B2, B2,
			 BE, B2, B2, B2, B2, B2, B2, B2, BE,
			 BE, B2, B2, B2, BS, B2, B2, B2, BE,
			 BE, BE, B1, B2, B2, B2, B1, BE, BE,
			 BE, BE, BE, B1, B1, B1, BE, BE, BE}
		},
		// Grand X - Level 9
		{
			"Grand X",
			{BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 BE, BE, BE, BE, BS, BE, BE, BE, BE,
			 B1, BB, BE, B2, B2, B2, BE, BB, B1,
			 B1, BE, BU, B3, B3, B3, BU, BE, B1,
			 BE, B2, B3, BU, B3, BU, B3, B2, BE,
			 B2, B2, B3, B3, BU, B3, B3, B2, B2,
			 BE, B2, B3, BU, B3, BU, B3, B2, BE,
			 B1, BE, BU, B3, B3, B3, BU, BE, B1,
			 B1, B1, BE, B2, B2, B2, BE, B1, B1,
			 B1, B1, B1, BE, B2, BE, B1, B1, B1,
			 B1, B1, B1, B1, BE, B1, B1, B1, B1}
		},
		// Shockwave - Level 10
		{
			"Shockwave",
			{BE, BE, B3, B3, B3, B3, B3, BE, BE,
			 BE, B3, B3, B3, B3, B3, B3, B3, BE,
			 B3, B3, B1, B1, BU, B1, B1, B3, B3,
			 B3, B1, BU, B1, BS, B1, BU, B1, B3,
			 B1, B1, B1, B2, BB, B2, B1, B1, B1,
			 B1, B2, B2, B2, BB, B2, B2, B2, B1,
			 B2, B2, BB, B1, B1, B1, BB, B2, B2,
			 B2, B1, B1, B1, B1, B1, B1, B1, B2,
			 B1, B1, B1, B1, B1, B1, B1, B1, B1,
			 B1, B1, B1, B1, B1, B1, B1, B1, B1,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE}
		},
		// Alleyways - Level 11
		{
			"Alleyways",
			{BE, BE, B3, BE, B3, BE, B3, BE, BE,
			 B3, BE, B3, BE, B3, BE, B3, BE, B3,
			 B3, BE, B3, BE, BB, BE, B3, BE, B3,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 B2, BE, B2, BE, B2, BE, B2, BE, B2,
			 B2, BE, B2, BE, B2, BE, B2, BE, B2,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 B1, BE, B1, BE, BB, BE, B1, BE, B1,
			 B1, BE, B1, BE, B1, BE, B1, BE, B1,
			 B1, BE, BU, BE, BU, BE, BU, BE, B1}
		},
		// Level 12
		{
			"Bo Bo Cha Cha",
			{BE, BE, B3, B3, BB, B3, B3, BE, BE,
			 BE, B3, B2, BE, BE, BE, B2, B3, BE,
			 B3, B2, B1, BE, BE, BE, B1, B2, B3,
			 B2, B1, B3, BE, BE, BE, B3, B1, B2,
			 B1, B3, B2, B3, BE, B3, B2, B3, B1,
			 B3, B2, B1, B2, BS, B2, B1, B2, B3,
			 B2, B1, B1, B1, BB, B1, B1, B1, B2,
			 B1, B1, B1, B1, BB, B1, B1, B1, B1,
			 B1, B1, B1, B1, B1, B1, B1, B1, B1,
			 B1, B1, B1, B1, B1, B1, B1, B1, B1,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE}
		},
		// HardBall - Level 13
		{
			"HardBall",
			{BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 BE, BE, BE, BE, BE, BE, BE, BE, BE,
			 BE, BE, BE, BB, B2, BB, BE, BE, BE,
			 BE, BE, BU, B2, B2, B2, BU, BE, BE,
			 BE, BU, B2, B2, B2, B2, B2, BU, BE,
			 BE, BU, B2, B2, B2, B2, B2, BU, BE,
			 BE, BU, B2, B2, B2, B2, B2, BU, BE,
			 BE, BE, BU, B2, B2, B2, BU, BE, BE,
			 BE, BE, BE, BU, BU, BU, BE, BE, BE,
			 B3, B3, B3, B3, B3, B3, B3, B3, B3,
			 B3, B3, B3, B3, B3, B3, B3, B3, B3}
		},
		// Rocket - Level 14
		{
			"Rocket",
			{BE, BB, BE, BE, BE, BE, BE, BE, BE,
			 BB, B2, BB, BE, BE, BE, B3, B3, B3,
			 B1, B2, B1, B2, B2, B2, B3, B1, B3,
			 B1, B1, B1, BE, BE, BE, B1, B3, B1,
			 B1, B1, B1, BE, BE, BE, B3, B1, B3,
			 B1, B1, B1, BE, BE, BE, B1, B3, B1,
			 B1, B1, B1, B2, B2, B2, B3, B1, B3,
			 B1, BB, B1, BE, BE, BE, B1, B3, B1,
			 B1, BB, B1, BE, BE, BE, B3, B1, B3,
			 B1, BB, B1, BE, BE, BE, B1, B3, B1,
			 B1, BS, B1, BE, BE, BE, B3, B3, B3}
		}
	};
