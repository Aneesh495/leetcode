defmodule Solution do
  @spec max_repeating(sequence :: String.t, word :: String.t) :: integer
  def max_repeating(sequence, word) do
    extend(sequence, word, word, 1)
  end

  defp extend(sequence, word, candidate, count) do
    if String.contains?(sequence, candidate) do
      extend(sequence, word, candidate <> word, count + 1)
    else
      count - 1
    end
  end
end