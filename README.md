## Valence

Valence returns following results:
- only negative
- mostly negative
- mostly neutral
- mostly positive
- only positive
- only neutral
- mostly mixed
- only mixed

## Running locally

Run `docker-compose -f docker-compose-valence.yml up`. Provide input like it is visible in the file system.

## When developing

- change valence-analyzer to valence in `docker-compose-valence.yml`
- Comment out line 3 in `Dockerfile-valence`
- Run `docker-compose -f docker-compose-build-valence.yml up --build`
- Comment in line 13 in `docker-compose-valence.yml`
- Run `docker-compose -f docker-compose-valence.yml up --build`
