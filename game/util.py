import neat
import pygame

from base import Base
from bird import Bird
from constants import bg_img, DRAW_LINES, STAT_FONT, WINDOW_WIDTH, FLOOR
from pipe import Pipe


def run(config_file):
    """
    Method to run the NEAT algorithm and train  neural network to play flappy bird.
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    # Create  population
    p = neat.Population(config)

    # show progress.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # run for up to 50 generations.
    winner = p.run(eval_genomes, 50)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))


def eval_genomes(genomes, config):
    """
    The method runs simulation of the current population of
    birds and stored their distance from the start point.
    """
    from constants import WIN, gen
    global WIN, gen
    win = WIN
    gen += 1

    nets = []
    birds = []
    ge = []
    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        ge.append(genome)

    base = Base(FLOOR)
    pipes = [Pipe(700)]
    score = 0

    clock = pygame.time.Clock()

    run = True
    while run and len(birds) > 0:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[
                0].PIPE_TOP.get_width():
                pipe_ind = 1
        for x, bird in enumerate(birds):
            ge[x].fitness += 0.1
            bird.move()
            output = nets[birds.index(bird)].activate(
                (bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))
            if output[
                0] > 0.5:
                bird.jump()
        base.move()

        rem = []
        add_pipe = False
        for pipe in pipes:
            pipe.move()
            for bird in birds:
                if pipe.collide(bird, win):
                    ge[birds.index(bird)].fitness -= 1
                    nets.pop(birds.index(bird))
                    ge.pop(birds.index(bird))
                    birds.pop(birds.index(bird))

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

        if add_pipe:
            score += 1
            for genome in ge:
                genome.fitness += 5
            pipes.append(Pipe(WINDOW_WIDTH))

        for r in rem:
            pipes.remove(r)

        for bird in birds:
            if bird.y + bird.img.get_height() - 10 >= FLOOR or bird.y < -50:
                nets.pop(birds.index(bird))
                ge.pop(birds.index(bird))
                birds.pop(birds.index(bird))

        window_draw(WIN, birds, pipes, base, score, gen, pipe_ind)


def displayRotateCenter(surf, image, topleft, angle):
    """
    Rotate a surface and display it to the window.
    Params: surf(surface to display), image, topLeft and angle(float).
    """
    rotated = pygame.transform.rotate(image, angle)
    rectangle = rotated.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated, rectangle.topleft)


def window_draw(win, birds, pipes, base, score, gen, pipe_ind):
    """
    Method to draw window for the main game loop.
    Params: win, bird(bird object), pipes (list of pipes), score(int), gen(current generation),
    pipe_ind(index of the closest pipe).

    """
    if gen == 0:
        gen = 1
    win.blit(bg_img, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)
    for bird in birds:
        if DRAW_LINES:
            try:
                pygame.draw.line(win, (255, 0, 0),
                                 (bird.x + bird.img.get_width() / 2, bird.y + bird.img.get_height() / 2),
                                 (pipes[pipe_ind].x + pipes[pipe_ind].PIPE_TOP.get_width() / 2, pipes[pipe_ind].height),
                                 5)
                pygame.draw.line(win, (255, 0, 0),
                                 (bird.x + bird.img.get_width() / 2, bird.y + bird.img.get_height() / 2), (
                                     pipes[pipe_ind].x + pipes[pipe_ind].PIPE_BOTTOM.get_width() / 2,
                                     pipes[pipe_ind].bottom), 5)
            except:
                pass
        bird.draw(win)

    #  display score
    score_label = STAT_FONT.render("Points: " + str(score), 1, (255, 255, 255))
    win.blit(score_label, (WINDOW_WIDTH - score_label.get_width() - 15, 10))

    score_label = STAT_FONT.render("Alive: " + str(len(birds)), 1, (255, 255, 255))
    win.blit(score_label, (10, 10))

    pygame.display.update()