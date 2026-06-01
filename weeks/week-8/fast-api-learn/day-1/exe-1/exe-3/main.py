from fastapi import FastAPI
import uvicorn



grades = {
"1": {"name": "Moshe", "grade": 88},
"2": {"name": "Yaakov", "grade": 75},
"3": {"name": "David", "grade": 92},
}

app = FastAPI()


@app.get('/students')
def get_students():
    return grades

@app.get('/students/top')
def get_top_student()->dict:
    """
    return the student dict with the best user
    
    """
    max_student_id = max(grades,key=lambda k:grades[k]['grade'])
    return grades[max_student_id]

@app.get('/students/count')
def get_student_count():
    """
    return the cnt grades
    """
    return len(grades)


@app.get('/students/average')
def get_average():
    """
    return the avg grades 
    
    """
    grades_sum = sum([d['grade'] for d in grades.values()])
    grades_average = grades_sum/ get_student_count()
    return {'grades_average':grades_average}



@app.get('/students/{student_id}')
def get_student(student_id:str):
    if student_id in grades:
        return grades[student_id] 
    else:
        return {'status':'not_found_id'}
    
    


if __name__ == "__main__":
    uvicorn.run(app=f'{__name__}:app', port=8050, reload=True)