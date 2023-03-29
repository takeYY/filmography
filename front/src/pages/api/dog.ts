type DogAPI = {
  message: string;
  status: string;
};

export const searchDog = async () => {
  const response = await fetch("https://dog.ceo/api/breeds/image/random");
  const res: DogAPI = await response.json();
  return res;
};
