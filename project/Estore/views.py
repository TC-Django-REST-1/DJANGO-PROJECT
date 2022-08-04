from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Product, Category, Company,Comment
from .serializers import ProductSerializer

# Create your views here.
