# Plotting power in the frequencyuency domain
fft_output = fft.fft(resid)
power = np.abs(fft_output)
frequency = fft.fftfrequency(len(resid))

mask = frequency >= 0
frequency, power = frequency[mask], power[mask]

plt.figure(figsize=(10, 4) )

ax1 = plt.subplot( 1, 2, 1 )
ax1.plot(frequency, power, label='resid')
ax1.set_title('All frequencies')
ax1.set_ylabel( 'Amplitude' )
ax1.set_xlabel( 'frequency[1 / Hour]' )
plt.xticks(rotation=90)

ax2 = plt.subplot( 1, 2, 2 )
mask = (frequency > 0) & (frequency <= 0.25)
ax2.plot(frequency[mask], power[mask])
ax2.set_title('frequencyuencies in (0, 0.25]')
ax2.set_ylabel( 'Amplitude' )
ax2.set_xlabel( 'frequencyuency [1 / Hour]' )

peaks = sig.find_peaks(power)[0]
peak_frequency =  frequency[peaks]
peak_power = power[peaks]
plt.plot(peak_frequency, peak_power, 'ro')

plt.tight_layout()
plt.xticks(rotation=90)
