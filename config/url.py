__author__ = 'yuetingqian'

pre_fix = 'controllers.'
urls = (
        "/", pre_fix + "index.Index",

        "/test", pre_fix + "test.Index",

        "/404", pre_fix + "error.NotFound",
)
