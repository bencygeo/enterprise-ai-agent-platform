def get_pod_logs(pod_name):
    return f"Pod {pod_name} logs: CrashLoopBackOff error"


def get_metrics(service):
    return f"High CPU usage detected in {service}"