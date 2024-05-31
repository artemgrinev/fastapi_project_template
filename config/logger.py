from loguru import logger

logger.add(
        "logs.json",
        format="{level} {time} {message}",
        level="DEBUG",
        rotation="10 mb",
        compression="zip",
        serialize=True,
)