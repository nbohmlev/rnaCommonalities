#!/usr/bin/env python
from rnaMotifs.getMirDbOutputSrc import mirDbBotWrapper as MB
if __name__=='__main__':
	mirName = 'mmu-miR-380-5p'
	MB.mirDbBotWrapper(mirName)
