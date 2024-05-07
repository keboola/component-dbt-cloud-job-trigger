def assign_status_data(data):
    return {
        "id": data.get("id"),
        "trigger_id": data.get("trigger_id"),
        "account_id": data.get("account_id"),
        "project_id": data.get("project_id"),
        "job_definition_id": data.get("job_definition_id"),
        "status": data.get("status"),
        "git_branch": data.get("git_branch"),
        "git_sha": data.get("git_sha"),
        "status_message": data.get("status_message"),
        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at"),
        "dequeued_at": data.get("dequeued_at"),
        "started_at": data.get("started_at"),
        "finished_at": data.get("finished_at"),
        "last_checked_at": data.get("last_checked_at"),
        "last_heartbeat_at": data.get("last_heartbeat_at"),
        "owner_thread_id": data.get("owner_thread_id"),
        "executed_by_thread_id": data.get("executed_by_thread_id"),
        "artifacts_saved": data.get("artifacts_saved"),
        "artifact_s3_path": data.get("artifact_s3_path"),
        "has_docs_generated": data.get("has_docs_generated"),
        "trigger": data.get("trigger"),
        "job": data.get("job"),
        "duration": data.get("duration"),
        "queued_duration": data.get("queued_duration"),
        "run_duration": data.get("run_duration"),
        "duration_humanized": data.get("duration_humanized"),
        "queued_duration_humanized": data.get("queued_duration_humanized"),
        "run_duration_humanized": data.get("run_duration_humanized"),
        "finished_at_humanized": data.get("finished_at_humanized"),
        "status_humanized": data.get("status_humanized"),
        "created_at_humanized": data.get("created_at_humanized")
    }


def assign_trigger_data(status_data):
    return {
        "id": status_data.get("id"),
        "trigger_id": status_data.get("trigger_id"),
        "account_id": status_data.get("account_id"),
        "project_id": status_data.get("project_id"),
        "job_definition_id": status_data.get("job_definition_id"),
        "status": status_data.get("status"),
        "git_branch": status_data.get("git_branch"),
        "git_sha": status_data.get("git_sha"),
        "status_message": status_data.get("status_message"),
        "created_at": status_data.get("created_at"),
        "updated_at": status_data.get("updated_at"),
        "dequeued_at": status_data.get("dequeued_at"),
        "started_at": status_data.get("started_at"),
        "finished_at": status_data.get("finished_at"),
        "last_checked_at": status_data.get("last_checked_at"),
        "last_heartbeat_at": status_data.get("last_heartbeat_at"),
        "owner_thread_id": status_data.get("owner_thread_id"),
        "executed_by_thread_id": status_data.get("executed_by_thread_id"),
        "artifacts_saved": status_data.get("artifacts_saved"),
        "artifact_s3_path": status_data.get("artifact_s3_path"),
        "has_docs_generated": status_data.get("has_docs_generated"),
        "trigger": status_data.get("trigger"),
        "job": status_data.get("job"),
        "duration": status_data.get("duration"),
        "queued_duration": status_data.get("queued_duration"),
        "run_duration": status_data.get("run_duration"),
        "duration_humanized": status_data.get("duration_humanized"),
        "queued_duration_humanized": status_data.get("queued_duration_humanized"),
        "run_duration_humanized": status_data.get("run_duration_humanized"),
        "finished_at_humanized": status_data.get("finished_at_humanized"),
        "status_humanized": status_data.get("status_humanized"),
        "created_at_humanized": status_data.get("created_at_humanized"),
        "scribe_enabled": status_data.get("scribe_enabled"),
    }