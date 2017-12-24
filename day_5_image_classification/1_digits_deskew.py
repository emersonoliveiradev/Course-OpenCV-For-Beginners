def deskew(img):
    m = cv2.moments(img)
    if abs(m['mu02']) < 1e-2:
        # no deskewing needed.
        return img.copy()
    # Calculate skew based on central momemts.
    skew = m['mu11']/m['mu02']
    # Calculate affine transform to correct skewness.
    M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
    # Apply affine transform
    img = cv2.warpAffine(img, M, (SZ, SZ),
          flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)
    return img


winSize = (20, 20)
blockSize = (8, 8)
blockStride = (4, 4)
cellSize = (8, 8)
nbins = 9
derivAperture = 1
winSigma = -1.
histogramNormType = 0
L2HysThreshold = 0.2
gammaCorrection = 1
nlevels = 64
signedGradient = True

hog = cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, nbins,
                        derivAperture, winSigma, histogramNormType, L2HysThreshold,
                        gammaCorrection, nlevels, useSignedGradients)

descriptor = hog.compute(im)


def svmInit(C=12.5, gamma=0.50625):
    model = cv2.ml.SVM_create()
    model.setGamma(gamma)
    model.setC(C)
    model.setKernel(cv2.ml.SVM_RBF)
    model.setType(cv2.ml.SVM_C_SVC)

    return model


def svmTrain(model, samples, responses):
    model.train(samples, cv2.ml.ROW_SAMPLE, responses)
    return model


def svmPredict(model, samples):
    return model.predict(samples)[1].ravel()