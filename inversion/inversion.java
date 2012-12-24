/**
 * Algorithms: Design and Analysis Part 1, Coursera
 * Problem 1: Counting the number of inversions in O(nlogn) time
 * This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some random order, with no integer repeated.
 * Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
 * @author Khoa Tran
 */

import java.io.*;
import java.util.Scanner;
import java.util.Arrays;

public class inversion {

    /**
     * Counts the number of inversions using divide and conquer in nlogn time
     * @param arr the original int array
     * @param n the length of the array
     * @return the number of inversions in nlogn time
     */
    public static long countInversion(int[] arr) {
        int len = arr.length;
        if (len < 2)
            return 0;
        else {
            int middle = len / 2, k;
            int[] left = Arrays.copyOfRange(arr, 0, middle);
            int[] right = Arrays.copyOfRange(arr, middle, len);

            /* Counts left and right inversions */
            long countLeft = countInversion(left);
            long countRight = countInversion(right);

            /* Counts the split inversions*/
            int[] result = new int[len];
            long countSplit = countSplitInversion(left, right, result);

            /* Copy back into the original array and return the number of inversions */
            for (k = 0; k < len; ++k)
               arr[k] = result[k];
            return countLeft + countRight + countSplit;
        }
    }

    /**
     * Counts the number of split inversions, i.e. inversions that occur in both halves of the array 
     * @param left the left side of the original int array
     * @param right the right side of the original int array
     * @param n the length of the array
     * @return the number of split inversions
     */
    private static long countSplitInversion(int[] left, int[] right, int[] result) {
        int i = 0, j = 0, k = 0;
        long count = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j])
                result[k++] = left[i++];
            else {
                result[k++] = right[j++];
                count += left.length - i;
            }
        }

        if (j == right.length) { // right is fully copied 
            while (i < left.length)
                result[k++] = left[i++];
        }
        else {
            while (j < right.length)
                result[k++] = right[j++];
        }
        return count; 
    }

    /**
     * Counts the number of lines in a text file
     * @param filename the name of the text file
     * @throws IOException when the file cannot be opened
     * @return the number of lines in the text file
     */
    public static int countLines(String filename) throws IOException {
        InputStream is = new BufferedInputStream(new FileInputStream(filename));
        try {
            byte[] c = new byte[1024];
            int count = 0;
            int readChars = 0;
            boolean empty = true;
            while ((readChars = is.read(c)) != -1) {
                empty = false;
                for (int i = 0; i < readChars; ++i) {
                    if (c[i] == '\n')
                        ++count;
                }
            }
            return (count == 0 && !empty) ? 1 : count;
        } finally {
            is.close();
        }
    }
    
    /**
     * Main method
     */ 
    public static void main(String [] args) {
        File file = new File("IntegerArray.txt");
        int temp, k = 0;
        int count = 0;

        /* Count the number of lines in the text file to find the correct array's size */
        try {
            count = countLines("IntegerArray.txt");
        }
        catch (IOException e) {
            System.out.println("File not found!");
            System.exit(-1);
        }

        /* Read in every number in the text file line by line */
        int arr[] = new int[count];
        try {
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) 
            {
                temp = scanner.nextInt();
                scanner.nextLine();
                arr[k] = temp;
                k++;
            }
        } 
        catch (FileNotFoundException e) 
        {
            e.printStackTrace();
        }
        
        System.out.println("Current size: " + arr.length);
        System.out.println("Number of inversions of array arr: " + countInversion(arr));
    }
}
