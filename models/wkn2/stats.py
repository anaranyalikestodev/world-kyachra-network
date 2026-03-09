from flask import Blueprint,render_template,redirect,url_for,flash
from flask import abort,request,jsonify,session

stats_bp=Blueprint