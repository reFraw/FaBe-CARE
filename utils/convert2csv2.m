clear
clc
close all

subject_ID = input(">>> INSERT SUBJECT ID (00 TO 04): ","s");

mat_path = strcat("C:\Users\fabra\Desktop\misc\EEG\data\subject_", ...
    num2str(subject_ID), ...
    ".mat");

data = load(mat_path);
data = struct2cell(data);
data = cell2mat(data);

t1 = data(:,1);

day_sec = 86400;
nSample = day_sec;

r_factor = 6;

check = 1;

while check

    channel = input(">>> INSERT CHANNEL (2 to 18): ");
    
    eeg = data(:, channel);

    figure
    plot(t1, eeg);
    grid on

    check = input(">>> INSERT 0 TO CONFIRM OR 1 TO SELECT ANOTHER CHANNEL: ");

    close all

end

eeg = repmat(eeg, r_factor, 1);

decimation_factor = floor(length(eeg)/nSample);
eeg = downsample(eeg, decimation_factor);
eeg = eeg(1:nSample);

t1 = datetime(2023, 05, 29, 00, 00, 00);
t2 = datetime(2023, 05, 30, 00, 00, 00);

t = linspace(t1, t2, nSample);
t = t';

fig = figure();
fig.WindowState = 'maximized';
plot(t, eeg, LineWidth=1.5);
grid on

save_path = strcat("csv_data/subject_", num2str(subject_ID), ".xlsx");

Tmin = input(">>> INSERT MIN TEMPERATURE: ");
Tmax = input(">>> INSERT MAX TEMPERATURE: ");
Fmin = input(">>> INSERT MIN FREQUENCY: ");
Fmax = input(">>> INSERT MAX FREQUENCY: ");
PSmin = input(">>> INSERT MIN P_sis: ");
PSmax = input(">>> INSERT MAX P_sis: ");
PDmin = input(">>> INSERT MIN P_dia: ");
PDmax = input(">>> INSERT MAX P_dia: ");


AnonID = input(">>> INSERT ANONIMYZED IDENTIFIER (AAAABBBCCC): ", "s");


% INSERT EEG DATA INTO XLSX
type = {'EEG'};
type = repmat(type, nSample, 1);

xlswrite(save_path, {"ID"}, 1, "A1");
xlswrite(save_path, {"Timestamp"}, 1, "B1");
xlswrite(save_path, {"Type"}, 1, "C1");
xlswrite(save_path, {"Value"}, 1, "D1");
xlswrite(save_path, {"Warning"}, 1, "E1");

ID = {AnonID};
ID = repmat(ID, 86496, 1);
xlswrite(save_path, ID, 1, "A2:A86497");

xlswrite(save_path, exceltime(t), 1, "B2:B86401");
xlswrite(save_path, type, 1, "C2:C86401");
xlswrite(save_path, eeg, 1, "D2:D86401");
xlswrite(save_path, {'N'}, 1, "E2:E86401");

% INSERT OTHER DATA
% 1. TEMPERATURE
type = {'T'};
type = repmat(type, 24, 1);

t_temp_pres = linspace(t1, t2, 24);
randomT = randi([Tmin Tmax], 24, 1);
warningT = {};
T_soglia = 38;
for i = 1 : length(randomT)
    if randomT(i) > T_soglia
        warningT(i) = {'Y'};
    else
        warningT(i) = {'N'};
    end
end

xlswrite(save_path, exceltime(t_temp_pres'), 1, "B86402:B86425")
xlswrite(save_path, type, 1, "C86402:C86425")
xlswrite(save_path, randomT, 1, "D86402:D86425")
xlswrite(save_path, warningT', 1, "E86402:E86425")

% 2. FREQUENCY
type = {'F'};
type = repmat(type, 24, 1);

randomF = randi([Fmin Fmax], 24, 1);
warningF = {};
F_soglia_max = 20;
F_soglia_min = 12;
for i = 1 : length(randomT)
    if (randomF(i) > F_soglia_max) || (randomF(i) < F_soglia_min)
        warningF(i) = {'Y'};
    else
        warningF(i) = {'N'};
    end
end

xlswrite(save_path, exceltime(t_temp_pres'), 1, "B86426:B86449")
xlswrite(save_path, type, 1, "C86426:C86449")
xlswrite(save_path, randomF, 1, "D86426:D86449")
xlswrite(save_path, warningF', 1, "E86426:E86449")

% 3. P DIAST
type = {'PD'};
type = repmat(type, 24, 1);

randomPD = randi([PDmin PDmax], 24, 1);
warningPD = {};
PD_soglia_min = 60;
PD_soglia_max = 90;
for i = 1 : length(randomT)
    if (randomPD(i) < PD_soglia_min) || (randomPD(i) > PD_soglia_max)
        warningPD(i) = {'Y'};
    else
        warningPD(i) = {'N'};
    end
end

xlswrite(save_path, exceltime(t_temp_pres'), 1, "B86450:B86473")
xlswrite(save_path, type, 1, "C86450:C86473")
xlswrite(save_path, randomPD, 1, "D86450:D86473")
xlswrite(save_path, warningPD', 1, "E86450:E86473")

% 4. P SIST
type = {'PS'};
type = repmat(type, 24, 1);

randomPS = randi([PSmin PSmax], 24, 1);
warningPS = {};
PS_soglia_min = 80;
PS_soglia_max = 150;
for i = 1 : length(randomT)
    if (randomPS(i) < PS_soglia_min) || (randomPS(i) > PS_soglia_max)
        warningPS(i) = {'Y'};
    else
        warningPS(i) = {'N'};
    end
end

xlswrite(save_path, exceltime(t_temp_pres'), 1, "B86474:B86497")
xlswrite(save_path, type, 1, "C86474:C86497")
xlswrite(save_path, randomPS, 1, "D86474:D86497")
xlswrite(save_path, warningPS', 1, "E86474:E86497")


fprintf("[INFO] Finished\n\n");