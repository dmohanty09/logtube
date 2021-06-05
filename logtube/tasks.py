from celery import shared_task, group

from logtube.scraper import YoutubeScraper, transcribe_video


@shared_task
def crawl_videos(video_ids):
    job = group(transcribe_single_video.s(video_id) for video_id in video_ids)
    result = job.apply_async()
    print(f'Crawl Videos result: {result}')

    return video_ids


@shared_task
def crawl_most_popular():
    api = YoutubeScraper()
    total_video_ids = get_pages(api)
    return total_video_ids


def get_pages(api, total_video_ids=[], next_page_token=None):
    response = api.get_most_popular(next_page_token)
    print(f"Video List response: {response}")

    video_ids = list(map(lambda v: v['id'], response['items']))

    # task = crawl_videos.delay(video_ids)
    sub_task = crawl_videos.s(video_ids).delay()
    print(f'Crawl Task: {sub_task.task_id}')
    total_video_ids.extend(video_ids)

    if 'nextPageToken' in response or len(total_video_ids) < response['pageInfo']['totalResults']:
        return get_pages(api, total_video_ids, response['nextPageToken'])
    else:
        return total_video_ids


@shared_task
def transcribe_single_video(video_id):
    transcript = transcribe_video(video_id)
    print(f'Transcript length: {len(transcript)}')
    return transcript
