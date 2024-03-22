import pygame
from datetime import datetime

pygame.init()
surface = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mickey Clock")
bg = pygame.image.load(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab7\MickeyClock\clock.png")
minArm = pygame.image.load(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab7\MickeyClock\left_minutes.png")
secArm = pygame.image.load(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab7\MickeyClock\right_seconds.png")
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        surface.blit(bg, (0, 0))

        t = datetime.now()
        sec = t.second
        min = t.minute


        s_ang = (60 -sec) * 6
        m_ang = (60-min) * 6

        rot_min_arm = pygame.transform.rotate(minArm, m_ang)
        rot_sec_arm = pygame.transform.rotate(secArm, s_ang)

        surface.blit(rot_min_arm, rot_min_arm.get_rect(center=(200, 200)))
        surface.blit(rot_sec_arm, rot_sec_arm.get_rect(center=(200, 200)))

        pygame.display.flip()
