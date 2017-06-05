from .models import Question
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.http import HttpResponse
from django.template import loader


def index(request):
    try:
        questions_count = 5
        latest_question_list = Question.objects.order_by(
            '-publication_date')[:questions_count]
    except Exception as error:
        print("ERROR getting Questions from DB: %s" % str(error))
        return None

    index_template_file = 'polls/index.html'
    template = loader.get_template(index_template_file)
    context = {
        'latest_question_list': latest_question_list,
        'questions_count': questions_count,
    }

    try:
        print("ddddddddddddddddddddd")
        rendered_response = template.render(context, request)
        print("AAAAAAAAAAAAAAAAA")
        http_response = HttpResponse(rendered_response)
        print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    except Exception as error:
        print("ERROR getting http respoonse: %s" % str(error))
        return None
    return http_response




def index1(request):
    try:
        questions_count = 5
        latest_question_list = Question.objects.order_by(
            '-publication_date')[:questions_count]
    except Exception as error:
        print("ERROR getting Questions from DB: %s" % str(error))
        return None

    index_template_file = 'polls/index.html'
    context = {
        'latest_question_list': latest_question_list,
        'questions_count': questions_count,
    }
    print("INFO: %s" % str(latest_question_list))
    try:
        print("#######################################", request, index_template_file, context)
        http_response = render(request, index_template_file, context)
        # http_response = HttpResponse("Test")
        print("********************************************************")
    except Exception as error:
        print("ERROR getting http response: %s" % str(error))
        return None
    return http_response


def detail(request, question_id):

    question_object = get_object_or_404(Question, pk=question_id)
    index_template_file = 'polls/detail.html'
    context = {
        'question_id': question_id,
        'question': question_object,
    }

    try:
        http_response = render(request, index_template_file, context)
    except Exception as error:
        print("ERROR getting http response: %s" % str(error))
        return None

    return http_response


def results(request, question_id):
    response = "You're looking at the results of question %s." % question_id
    try:
        http_response = HttpResponse(response)
    except Exception as error:
        print("ERROR: %s" % str(error))
        return None
    return http_response


def vote(request, question_id):
    response = "You're voting on question %s." % question_id
    try:
        http_response = HttpResponse(response)
    except Exception as error:
        print("ERROR: %s" % str(error))
        return None
    return http_response
