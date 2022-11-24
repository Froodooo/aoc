const openCharacters = ["(", "[", "{", "<"];

function getCloseCharacter(character: string): string {
  switch (character) {
    case "(":
      return ")";
    case "[":
      return "]";
    case "{":
      return "}";
    case "<":
      return ">";
    default:
      return "";
  }
}

export function readChunk(
  line: string[],
  closeCharacters: string[],
  haltOnError = true,
): string[] {
  const restLine = line.splice(1);
  const [currentCharacter] = line;

  if (openCharacters.includes(currentCharacter)) {
    closeCharacters.push(getCloseCharacter(currentCharacter));
    return readChunk(restLine, closeCharacters, haltOnError);
  }

  const closeCharacter = closeCharacters.pop();
  if (currentCharacter === closeCharacter) {
    return readChunk(restLine, closeCharacters, haltOnError);
  } else {
    if (haltOnError) {
      return [currentCharacter];
    } else {
      if (closeCharacter) closeCharacters.reverse().unshift(closeCharacter);
      return closeCharacters;
    }
  }
}
