import moviepy.editor as mpy
import numpy
import random

class VideoManager:

    @staticmethod
    def generate_video(image) -> str:
        audio_track = random.randint(1, 4)
        audio_clip = mpy.AudioFileClip(f"./music/{audio_track}.mp3")

        image_clip = mpy.ImageClip(numpy.array(image), duration=audio_clip.duration)
        image_clip = VideoManager.fix_image_clip(image_clip)
        image_clip = (image_clip.set_position(("center", "center"))
                        .set_audio(audio_clip) )

        background_track = random.randint(1, 4)
        background_clip: mpy.VideoFileClip = ( mpy.VideoFileClip(f"./backgrounds/{background_track}.mp4")
                            .subclip(0, audio_clip.duration)
                            .resize((image_clip.w + 80, image_clip.h + 100)) )

        final = mpy.CompositeVideoClip([background_clip, image_clip])
        final.write_videofile('./temp/movie.mp4', fps=24)
        return "./temp/movie.mp4"

    @staticmethod
    def fix_image_clip(image_clip: mpy.ImageClip) -> mpy.ImageClip:
        """
        Moviepy for some reason breaks when the width or height is odd
        """
        if image_clip.w % 2 != 0:
            image_clip = image_clip.resize((image_clip.w + 1, image_clip.h))
        if image_clip.h % 2 != 0:
            image_clip = image_clip.resize((image_clip.w, image_clip.h + 1))
        return image_clip