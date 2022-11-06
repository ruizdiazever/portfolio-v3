#!/usr/bin/bash
(uvicorn main:app --reload & (cd ./frontend; npm run dev))