#!/usr/bin/python
import random
import re

MAX_CARDS = 54
MAX_CARDS_WITHOUT_JOKER = 52
CARDS_IN_ONE_SUIT=13
JOKER_CARDS = 2
BLACK_JOKER = 52# 0~53
RED_JOKER = 53 # 0~53

# HEART 
# SPADE
# DIAMOND
# CLUB

SUIT = {
	'HEART':1,
	'SPADE':2,
	'CLUB':3,
	'DIAMOND':4,
	'BLACK-JOKER':5,
	'RED-JOKER':6
}

# (48, 31, 38), (9, 7, 27)

def test_function():
	for i in range(5):
		yield (i,)


class poker():
	def __init__(self,count=1,joker=True):
		self.card_count = MAX_CARDS * count
		self.with_joker = joker
		if self.with_joker:
			self.cards = 2*range(MAX_CARDS)
		else:
			self.cards = range(MAX_CARDS - JOKER_CARDS)
		self.wash_cards()


	def numbers_to_suit_and_points(self,number):
		ret = {'suit':None,'points':None}

		if number == BLACK_JOKER:
			ret['suit'] = 'BLACK-JOKER'
		elif number == RED_JOKER:
			ret['suit'] = 'RED-JOKER'
		elif (number < CARDS_IN_ONE_SUIT):
			ret['suit'] = 'HEART'
			ret['points'] = (number%CARDS_IN_ONE_SUIT+1) # 0~12  ==> 1~13
		elif (number < 2*CARDS_IN_ONE_SUIT):
			ret['suit'] = 'SPADE'
			ret['points'] = (number%CARDS_IN_ONE_SUIT+1) # 0~12  ==> 1~13
		elif (number < 3*CARDS_IN_ONE_SUIT):
			ret['suit'] = 'CLUB'
			ret['points'] = (number%CARDS_IN_ONE_SUIT+1) # 0~12  ==> 1~13
		elif (number < 4*CARDS_IN_ONE_SUIT):
			ret['suit'] = 'DIAMOND'
			ret['points'] = (number%CARDS_IN_ONE_SUIT+1) # 0~12  ==> 1~13

		return ret

	def translate_card(number):
		return card

	def wash_cards(self):
		random.shuffle(self.cards)

	def print_cards(self):
		print self.card_count
		print self.cards

	def sort_cards(self, cards):
		return sorted(cards,reverse=True)

	def get_top_card(self):
		self.card_count -= 1
		return self.cards.pop()

	def get_poker_type(self,cards):
		final_cards = {}
		color_cards = {}
		number_cards = {}
		for card in cards:
			ret = self.numbers_to_suit_and_points(card)
			color_cards.setdefault(ret['suit'], [])
			number_cards.setdefault(ret['points'], [])
			color_cards[ret['suit']].insert(0,ret['points'])
			number_cards[ret['points']].insert(0,ret['suit'])

		final_cards['color'] = color_cards
		final_cards['number'] = number_cards

		print final_cards
		print final_cards['number']
		print len(final_cards['number'])
		print len(cards)
		
		if (len(final_cards['number']) == len(cards)):
			cards_type = 'single'# sorted is ok
			# QK1 is not calced
			while True:
				lastkey = sorted(final_cards['number'].keys())
				

			if (len(final_cards['color']) == len(cards) - 2):
				cards_type = 'same_color'# sorted is ok

		elif (len(final_cards['number']) == (len(cards) - 1)):
			cards_type = 'pairs'# 
		elif (len(final_cards['number']) == (len(cards) - 2)):
			cards_type = 'three'#

		
		print cards_type
		
	#	for number in final_cards['number']:
		#	print number

	def deal_cards(self,count=1, peoples=1):
		print "deal_cards, count =",count,",peoples=",peoples
		if count == 1:
			for p in range(peoples):
				yield (self.get_top_card(),)
		else:
			for i in self.deal_cards(count-1,peoples):
				yield (self.get_top_card(),) + i

def testfuc():
	p = poker(1,False)

	ret = p.deal_cards(count=3,peoples=1)
	
	for x in ret:
		print p.sort_cards(x)
		p.get_poker_type(x)

testfuc()
