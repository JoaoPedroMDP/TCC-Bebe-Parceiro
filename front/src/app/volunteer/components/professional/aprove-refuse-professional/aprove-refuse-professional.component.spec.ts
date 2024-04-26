import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AproveRefuseProfessionalComponent } from './aprove-refuse-professional.component';

describe('AproveRefuseProfessionalComponent', () => {
  let component: AproveRefuseProfessionalComponent;
  let fixture: ComponentFixture<AproveRefuseProfessionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AproveRefuseProfessionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AproveRefuseProfessionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
