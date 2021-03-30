#!/usr/bin/env python
#coding: utf-8



class ABEL():

    def __init__(self, init_lr, epoc_step, last_decay_epoc, warmup_steps = None, warmup_lr = None):
        self.init_lr = init_lr
        self.warmup_steps = warmup_steps
        self.warmup_lr = warmup_lr
        self.now_lr = init_lr
        self.all_wnorm = []
        self.reached_minima = False
        self.decay_factor = 0.5
        self.epoc_step = epoc_step
        self.last_decay_epoc = last_decay_epoc


    def get_now_lr(self, now_wnorm, now_step_num):
        if self.warmup_steps and self.warmup_lr:
            if now_step_num <= self.warmup_steps:
                self.now_lr = self.warmup_lr + (self.init_lr -self.warmup_lr) * (now_step_num) / float(self.warmup_steps)
                return self.now_lr

        if now_step_num % 200 != 0:
            return self.now_lr

        if len(self.all_wnorm) == 3:
            del self.all_wnorm[0]
        self.all_wnorm.append(now_wnorm)

        if len(self.all_wnorm) < 3:
            return self.now_lr

        if (self.all_wnorm[-1] - self.all_wnorm[-2]) * (self.all_wnorm[-2] - self.all_wnorm[-3]) < 0 and\
                (self.all_wnorm[-2] > self.all_wnorm[-1]):
            self.now_lr = self.now_lr * self.decay_factor

        if now_step_num > self.epoc_step * self.last_decay_epoc:
            self.now_lr = self.now_lr * self.decay_factor

        return self.now_lr



