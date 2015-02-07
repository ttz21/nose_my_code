try:
    raise(Exception())
except Exception as exc:
    import ipdb; ipbd.set_trace()
