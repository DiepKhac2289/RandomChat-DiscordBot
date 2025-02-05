import os
import asyncio
import discord
import random

os.system('pip install -U discord==1.7.3')
os.system('pip install -U discord.py==1.7.3')


token = "your-token-id"  # yourTokenId
channelId = "channel-id"  # channeild


mainMessages = [
    "Morning guys! Do I miss any big news today?",
    "I hear people talking about us outside, they said that this project is good haha?",
    "Haha you are so fun guys, make some noise here",
    "Let's keep the energy up! Every message makes this space better!",
    "What's up today? We have any plans today guys?",
    "I'm so hungry lol but I can not stop chatting with you",
    "Need coffee asap, omg ",
    "The more we chat, the stronger our community gets! Keep it up!",
    "Chill vibes today!",
    "So not quiet here ",
    "Wow, time flies!",
    "A thriving community starts with you! Keep sharing and connecting!",
    "What's everyone doing?",
    "happy day with story soon! ",
    "I should be working lol",
    "Your messages bring life to this chat! Let's keep it fun and engaging!",
    "This momment is wild ",
    "the day with best projest?",
    "Lol same here!",
    "Who else is bored?",
    "Engagement is key! Drop a message and keep the vibes going!",
    "Break time! Stretch a bit! ",
    "I'm sleepy again, wake me up guys ",
    "Haven't seen you in a while!",
    "We're building something amazing together! Keep the chat alive!",
    "Stay hydrated guys ",
    "make the best project strong again",
    "Any suggestions for me today, I will take a holliday with my friend in JP?",
    "Omg too many messages!",
    "Where's everyone from?",
    "Let's keep the momentum strong! Every message helps!",
    "Midnight thoughts hitting hard",
    "Good vibes only! ",
    "Bruh no way ",
    "Hope today's a good day!",
    "The best way to grow is to talk more! Let's keep it rolling!",
    "Every small effort counts! Keep pushing forward!",
    "Together, we can make this project a huge success!",
    "Your contribution matters! Lets keep the momentum going!",
    "Success is built on teamwork. Lets support each other!",
    "The more we engage, the stronger our community becomes!",
    "Work hard, play harder ",
    "Spamming? Nah just chatting",
    "We are all in this together! Lets keep the energy high!",
    "Great things take time, but with effort, we ll get there soon!",
    "Hard work always pays off! Lets keep going strong!",
    "Your support means everything! Lets keep pushing forward!",
    "Stay consistent, stay positive, and success will follow!",
    "This project is growing because of YOU! Keep it up!",
    "Okay, I need a nap ",
    "Your voice makes a difference! Let's keep building together!",
    "Send memes pls",
    "The road to success is built with every message we share!",
    "Lets make this the best community ever! Keep chatting!",
    "Life update anyone?",
    "Who else is working rn?",
    "Were building something amazing here. Keep up the great work!",
    "Your engagement fuels the projects growth! Keep supporting!",
    "Every message is a step toward an awesome community! Keep chatting!",
    "What a crazy day!",
    "You guys are fun lol",
    "Music makes everything better",
    "Can't believe it's already Feb!",
    "More chats = More fun! Let's keep the conversation alive!",
    "Any funny story here?",
    "Your support and engagement bring us closer to success!",
    "Together, we are unstoppable. Let us keep pushing forward!",
    "make some noise guys?",
    "Were on the path to success! Lets keep moving forward!",
    "Lets make history together! Keep the energy high!",
    "Good day to y'all!",
    "You are making a difference with every message you send!",
    "Success is within reach if we keep supporting each other!",
    "A strong community is built on active participation. Keep going!",
    "Motivation needed!",
    "A lively chat keeps the energy up! Keep the messages coming!",
    "Ugh, Monday tomorrow",
    "Today was so fast!",
    "Every effort you make helps this project grow stronger!",
    "Consistency and teamwork will lead us to great success!",
    "The more we share, the faster we grow as a community!",
    "I need weekend now, a lot of work to do, need take rest 😂",
    "Let us continue working together to achieve something amazing!",
    "Every conversation brings new ideas and opportunities!",
    "Your dedication is what makes this community thrive!",
     "A great community is created by people like you who stay engaged!",
    "The road to success is paved with teamwork and commitment!",
    "If we stay focused and work together, success is guaranteed!",
    "Wait what happened??",
    "Keep the momentum going, and soon we will see great results!",
    "Each message you send helps build a stronger foundation for success!",
    "Your participation is what makes this community special!",
    "A successful project needs passionate people like you!",
    "Laughing too hard rn ",
    "Your contribution is valuable, and together we will make it happen!",
    "Let us continue to support each other and grow stronger!",
    "The more we engage, the closer we get to reaching our goals!",
    "Success is built on daily efforts, and you are doing great!",
    "Okok you are not tired but I should sleep",
    "Sending good vibes to all!",
    "Let us continue building something incredible together!",
    "With effort and dedication, we are creating something amazing!",
    "The future looks bright because of the hard work we put in today!",
]

class Main(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        channel = self.get_channel(channelId)

        while True:
            message = random.choice(mainMessages)  # RandomMessage
            await channel.send(message)
            print(f'Sent message: {message}')
            
            delay = random.randint(30, 100)  # randomTime(second)
            await asyncio.sleep(delay)

    async def on_message(self, message):
        pass  # No Reply message

if __name__ == '__main__':
    Main().run(token, bot=False)
