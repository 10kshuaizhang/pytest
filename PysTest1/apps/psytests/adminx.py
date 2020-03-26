# -*- coding:utf-8 -*-
__author__ = '10k'
__date__ = '2/23/20'

import xadmin
from .models import MentalEvaluation, UserEvaluation, UserReviewForEvaluation, EvalQuestion, Options


class MentalEvaluationAdmin(object):
    list_display = ('eval_id', 'eval_type', 'title', 'intro', 'price', 'created_on',
                    'is_online', 'avatar', 'nums_eval', 'state', 'ques_num')
    search_fields = ('eval_id', 'eval_type', 'title', 'intro', 'price', 'created_on',
                     'is_online', 'avatar', 'nums_eval', 'state', 'ques_num')
    list_filter = ('eval_id', 'eval_type', 'title', 'intro', 'price', 'created_on',
                   'is_online', 'avatar', 'nums_eval', 'state', 'ques_num')
    data_charts = {
        "user_count": {'title': u"测评统计", "x-field": 'eval_id', "y-field": "price",
                       "order": ('created_on',)},
    }


xadmin.site.register(MentalEvaluation, MentalEvaluationAdmin)


class EvalQuestionAdmin(object):
    list_display = ('q_id', 'q_desc', 'eval', 'reverse_scoring', 'dimension')
    search_fields = ('q_id', 'q_desc', 'eval', 'reverse_scoring', 'dimension')
    list_filter = ('q_id', 'q_desc', 'eval', 'reverse_scoring', 'dimension')


xadmin.site.register(EvalQuestion, EvalQuestionAdmin)


class UserEvaluationAdmin(object):
    list_display = ('mentalEvaluation', 'user_id', 'eval_id', 'eval_score',
                    'user_count', 'eval_result', 'created_on', 'payment_status')
    search_fields = ('mentalEvaluation', 'user_id', 'eval_id', 'eval_score',
                     'user_count', 'eval_result', 'created_on', 'payment_status')
    list_filter = ('mentalEvaluation', 'user_id', 'eval_id', 'eval_score',
                   'user_count', 'eval_result', 'created_on', 'payment_status')


xadmin.site.register(UserEvaluation, UserEvaluationAdmin)


class OptionsAdmin(object):
    list_display = ('o_id', 'o_desc', 'question')
    search_fields = ('o_id', 'o_desc', 'question')
    list_filter = ('o_id', 'o_desc', 'question')


xadmin.site.register(Options, OptionsAdmin)


class UserReviewForEvaluationAdmin(object):
    list_display = ('eval_id', 'user_id', 'review', 'created_on')
    search_fields = ('eval_id', 'user_id', 'review', 'created_on')
    list_filter = ('eval_id', 'user_id', 'review', 'created_on')


xadmin.site.register(UserReviewForEvaluation, UserReviewForEvaluationAdmin)
