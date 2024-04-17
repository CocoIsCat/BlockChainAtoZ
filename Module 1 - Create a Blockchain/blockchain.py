# Module 1 - Create a Blockchain

# To be installed:
# Flask : pip install Flask
# Postman HTTP Client

# Importing the libraried

import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Building a Blockchain

class Blockchain:
    def __init__(self): # 초기화 함수
        self.chain = [] # 블록이 포함될 체인
        self.create_block(proof = 1, previous_hash = '0')   # 제네시스 블록 생성

    # 블록 생성
    def create_block(self, proof, previous_hash):
        block = { 'index' : len(self.chain) + 1,    # 몇번쨰 블록인지
                  'timestamp' : str(datetime.datetime.now()),   # 언제 생성된 블록인지
                  'proof' : proof,  # 자격 증명
                  'previous_hash' : previous_hash, } # 이전 해시
        self.chain.append(block)    # 체인에 블록 추가
        return block

    # 이전 블록 가져오기
    def get_previous_block(self):
        return self.chain[-1]
# Part 2 = Miging our Blockchain